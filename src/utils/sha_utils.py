"""SHA hash utilities and management."""

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Optional, Union


class SHAHashManager:
    """Manager for SHA hash operations including file hashing, verification, and caching."""

    def __init__(self, algorithm: str = "sha256"):
        """
        Initialize the SHA hash manager.

        Args:
            algorithm: SHA algorithm to use ('sha1', 'sha224', 'sha256', 'sha384', 'sha512')
        """
        self.algorithm = algorithm.lower()
        self._validate_algorithm()

    def _validate_algorithm(self) -> None:
        """Validate that the algorithm is supported."""
        supported_algorithms = ["sha1", "sha224", "sha256", "sha384", "sha512"]
        if self.algorithm not in supported_algorithms:
            raise ValueError(
                f"Unsupported algorithm: {self.algorithm}. "
                f"Supported algorithms: {supported_algorithms}"
            )

    def hash_string(self, text: str, encoding: str = "utf-8") -> str:
        """
        Generate SHA hash for a string.

        Args:
            text: String to hash
            encoding: Text encoding to use

        Returns:
            Hexadecimal hash string
        """
        hash_obj = hashlib.new(self.algorithm)
        hash_obj.update(text.encode(encoding))
        return hash_obj.hexdigest()

    def hash_file(self, file_path: Union[str, Path], chunk_size: int = 8192) -> str:
        """
        Generate SHA hash for a file.

        Args:
            file_path: Path to the file
            chunk_size: Size of chunks to read at a time

        Returns:
            Hexadecimal hash string

        Raises:
            FileNotFoundError: If file doesn't exist
            IOError: If file cannot be read
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not file_path.is_file():
            raise IOError(f"Path is not a file: {file_path}")

        hash_obj = hashlib.new(self.algorithm)

        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(chunk_size):
                    hash_obj.update(chunk)
        except IOError as e:
            raise IOError(f"Cannot read file {file_path}: {e}")

        return hash_obj.hexdigest()

    def hash_bytes(self, data: bytes) -> str:
        """
        Generate SHA hash for bytes data.

        Args:
            data: Bytes to hash

        Returns:
            Hexadecimal hash string
        """
        hash_obj = hashlib.new(self.algorithm)
        hash_obj.update(data)
        return hash_obj.hexdigest()

    def verify_file_hash(self, file_path: Union[str, Path], expected_hash: str) -> bool:
        """
        Verify that a file's hash matches the expected hash.

        Args:
            file_path: Path to the file
            expected_hash: Expected hash value

        Returns:
            True if hash matches, False otherwise
        """
        try:
            actual_hash = self.hash_file(file_path)
            return actual_hash.lower() == expected_hash.lower()
        except (FileNotFoundError, IOError):
            return False

    def verify_string_hash(
        self, text: str, expected_hash: str, encoding: str = "utf-8"
    ) -> bool:
        """
        Verify that a string's hash matches the expected hash.

        Args:
            text: String to verify
            expected_hash: Expected hash value
            encoding: Text encoding to use

        Returns:
            True if hash matches, False otherwise
        """
        actual_hash = self.hash_string(text, encoding)
        return actual_hash.lower() == expected_hash.lower()

    def create_hash_file(
        self,
        file_path: Union[str, Path],
        hash_file_path: Optional[Union[str, Path]] = None,
    ) -> Path:
        """
        Create a hash file containing the SHA hash of the input file.

        Args:
            file_path: Path to the file to hash
            hash_file_path: Path for the hash file (defaults to file_path + '.sha256')

        Returns:
            Path to the created hash file
        """
        file_path = Path(file_path)
        if hash_file_path is None:
            hash_file_path = file_path.with_suffix(
                file_path.suffix + f".{self.algorithm}"
            )
        else:
            hash_file_path = Path(hash_file_path)

        file_hash = self.hash_file(file_path)

        with open(hash_file_path, "w") as f:
            f.write(f"{file_hash}  {file_path.name}\n")

        return hash_file_path

    def verify_hash_file(
        self,
        file_path: Union[str, Path],
        hash_file_path: Optional[Union[str, Path]] = None,
    ) -> bool:
        """
        Verify a file against its hash file.

        Args:
            file_path: Path to the file to verify
            hash_file_path: Path to the hash file (defaults to file_path + '.sha256')

        Returns:
            True if verification passes, False otherwise
        """
        file_path = Path(file_path)
        if hash_file_path is None:
            hash_file_path = file_path.with_suffix(
                file_path.suffix + f".{self.algorithm}"
            )
        else:
            hash_file_path = Path(hash_file_path)

        if not hash_file_path.exists():
            return False

        try:
            with open(hash_file_path, "r") as f:
                hash_line = f.read().strip()
                expected_hash = hash_line.split()[0]
        except (IOError, IndexError):
            return False

        return self.verify_file_hash(file_path, expected_hash)

    def generate_and_save_hash(
        self,
        file_path: Union[str, Path],
        hash_file_path: Optional[Union[str, Path]] = None,
        format: str = "simple",
    ) -> Dict[str, Any]:
        """
        Generate hash for a file and save it to a hash file with metadata.

        Args:
            file_path: Path to the file to hash
            hash_file_path: Path for the hash file (defaults to file_path + '.{algorithm}')
            format: Output format ('simple', 'json', 'checksum')

        Returns:
            Dictionary containing hash information and saved file path
        """
        file_path = Path(file_path)
        if hash_file_path is None:
            hash_file_path = file_path.with_suffix(
                file_path.suffix + f".{self.algorithm}"
            )
        else:
            hash_file_path = Path(hash_file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Generate hash
        file_hash = self.hash_file(file_path)
        file_size = file_path.stat().st_size
        file_mtime = file_path.stat().st_mtime

        # Prepare hash data
        hash_data = {
            "algorithm": self.algorithm,
            "hash": file_hash,
            "file_path": str(file_path),
            "file_name": file_path.name,
            "file_size": file_size,
            "file_size_mb": round(file_size / (1024 * 1024), 2),
            "timestamp": file_mtime,
        }

        # Save hash file based on format
        if format == "simple":
            with open(hash_file_path, "w") as f:
                f.write(f"{file_hash}  {file_path.name}\n")
        elif format == "json":
            with open(hash_file_path, "w") as f:
                json.dump(hash_data, f, indent=2)
        elif format == "checksum":
            with open(hash_file_path, "w") as f:
                f.write(f"{file_hash}  {file_path.name}\n")
                f.write(f"# {self.algorithm.upper()} checksum for {file_path.name}\n")
                f.write(
                    f"# File size: {file_size} bytes ({hash_data['file_size_mb']} MB)\n"
                )
        else:
            raise ValueError(
                f"Unsupported format: {format}. Supported: simple, json, checksum"
            )

        hash_data["saved_to"] = str(hash_file_path)
        hash_data["format"] = format
        return hash_data

    def compare_hash_from_file(
        self,
        file_path: Union[str, Path],
        hash_file_path: Union[str, Path],
        format: str = "auto",
    ) -> Dict[str, Any]:
        """
        Compare a file's hash with a hash stored in a file.

        Args:
            file_path: Path to the file to verify
            hash_file_path: Path to the hash file
            format: Hash file format ('auto', 'simple', 'json', 'checksum')

        Returns:
            Dictionary containing comparison results
        """
        file_path = Path(file_path)
        hash_file_path = Path(hash_file_path)

        if not file_path.exists():
            return {
                "match": False,
                "error": "File not found",
                "file_path": str(file_path),
                "hash_file_path": str(hash_file_path),
            }

        if not hash_file_path.exists():
            return {
                "match": False,
                "error": "Hash file not found",
                "file_path": str(file_path),
                "hash_file_path": str(hash_file_path),
            }

        # Auto-detect format if not specified
        if format == "auto":
            try:
                with open(hash_file_path, "r") as f:
                    content = f.read().strip()
                    if content.startswith("{"):
                        format = "json"
                    elif content.startswith("#"):
                        format = "checksum"
                    else:
                        format = "simple"
            except Exception:
                format = "simple"

        # Read expected hash based on format
        try:
            with open(hash_file_path, "r") as f:
                if format == "json":
                    hash_data = json.load(f)
                    expected_hash = hash_data.get("hash", "")
                    stored_algorithm = hash_data.get("algorithm", "")
                    if stored_algorithm and stored_algorithm != self.algorithm:
                        return {
                            "match": False,
                            "error": f"Algorithm mismatch: expected {stored_algorithm}, got {self.algorithm}",
                            "file_path": str(file_path),
                            "hash_file_path": str(hash_file_path),
                        }
                else:  # simple or checksum format
                    lines = f.readlines()
                    # Find the hash line (skip comment lines)
                    hash_line = None
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            hash_line = line
                            break

                    if not hash_line:
                        return {
                            "match": False,
                            "error": "No hash found in file",
                            "file_path": str(file_path),
                            "hash_file_path": str(hash_file_path),
                        }

                    expected_hash = hash_line.split()[0]

        except Exception as e:
            return {
                "match": False,
                "error": f"Error reading hash file: {e}",
                "file_path": str(file_path),
                "hash_file_path": str(hash_file_path),
            }

        # Generate actual hash and compare
        try:
            actual_hash = self.hash_file(file_path)
            match = actual_hash.lower() == expected_hash.lower()

            return {
                "match": match,
                "file_path": str(file_path),
                "hash_file_path": str(hash_file_path),
                "expected_hash": expected_hash,
                "actual_hash": actual_hash,
                "algorithm": self.algorithm,
                "format": format,
            }
        except Exception as e:
            return {
                "match": False,
                "error": f"Error generating hash: {e}",
                "file_path": str(file_path),
                "hash_file_path": str(hash_file_path),
            }

    def get_hash_info(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Get comprehensive hash information for a file.

        Args:
            file_path: Path to the file

        Returns:
            Dictionary containing hash information
        """
        file_path = Path(file_path)

        if not file_path.exists():
            return {"error": "File not found"}

        try:
            file_hash = self.hash_file(file_path)
            file_size = file_path.stat().st_size

            return {
                "file_path": str(file_path),
                "algorithm": self.algorithm,
                "hash": file_hash,
                "file_size": file_size,
                "file_size_mb": round(file_size / (1024 * 1024), 2),
                "exists": True,
            }
        except Exception as e:
            return {
                "file_path": str(file_path),
                "algorithm": self.algorithm,
                "error": str(e),
                "exists": False,
            }

    def batch_hash_files(
        self,
        file_paths: list[Union[str, Path]],
        output_file: Optional[Union[str, Path]] = None,
    ) -> Dict[str, str]:
        """
        Generate hashes for multiple files.

        Args:
            file_paths: List of file paths to hash
            output_file: Optional file to save hash results as JSON

        Returns:
            Dictionary mapping file paths to their hashes
        """
        results = {}

        for file_path in file_paths:
            try:
                file_path = Path(file_path)
                hash_value = self.hash_file(file_path)
                results[str(file_path)] = hash_value
            except Exception as e:
                results[str(file_path)] = f"Error: {e}"

        if output_file:
            output_file = Path(output_file)
            with open(output_file, "w") as f:
                json.dump(results, f, indent=2)

        return results

    def __str__(self) -> str:
        """String representation of the hash manager."""
        return f"SHAHashManager(algorithm={self.algorithm})"

    def __repr__(self) -> str:
        """Detailed string representation of the hash manager."""
        return f"SHAHashManager(algorithm='{self.algorithm}')"


# Convenience functions for common operations
def quick_hash_file(file_path: Union[str, Path], algorithm: str = "sha256") -> str:
    """Quickly hash a file with the specified algorithm."""
    manager = SHAHashManager(algorithm)
    return manager.hash_file(file_path)


def quick_hash_string(text: str, algorithm: str = "sha256") -> str:
    """Quickly hash a string with the specified algorithm."""
    manager = SHAHashManager(algorithm)
    return manager.hash_string(text)


def verify_file_integrity(
    file_path: Union[str, Path], expected_hash: str, algorithm: str = "sha256"
) -> bool:
    """Quickly verify file integrity."""
    manager = SHAHashManager(algorithm)
    return manager.verify_file_hash(file_path, expected_hash)
