# Algorithm Testbed

A comprehensive testing framework for algorithm problems with organized test data, solutions, and documentation.

## 📁 Project Structure

```
testbed/
├── src/trials/                    # Algorithm solutions and tests
│   ├── dynamic_programming/       # DP problems
│   ├── greedy_algorithm/          # Greedy problems
│   ├── hashing_and_data_structures/ # Hash/DS problems
│   └── sorting_searching/         # Sorting/searching problems
├── data/                          # Test data with SHA verification
│   ├── dynamic_programming/       # DP test data (.parquet + .sha files)
│   ├── greedy_algorithm/          # Greedy test data
│   ├── hashing_and_data_structures/ # Hash/DS test data
│   └── sorting_searching/         # Sorting/searching test data
├── documents/                     # Problem documentation
│   ├── dynamic_programming/       # DP problem docs
│   ├── greedy_algorithm/          # Greedy problem docs
│   ├── hashing_and_data_structures/ # Hash/DS problem docs
│   └── sorting_searching/         # Sorting/searching problem docs
└── utils/                         # Shared utilities
```

## 🚀 Quick Start

### 1. Install uv (if needed)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Setup Project
```bash
# Clone and install
git clone <repository-url>
cd testbed
uv sync
uv run pre-commit install
```

### 3. Run Tests
```bash
# Run all tests
uv run pytest

# Run specific problem
uv run pytest src/trials/dynamic_programming/coin_change_test.py -v

# Generate test data
uv run testbed generate-test-data
```

That's it! 🎉

### Running Tests
```bash
# Run all tests (automatically generates test data first)
uv run pytest

# Run specific category
uv run pytest src/trials/dynamic_programming/

# Run specific problem
uv run pytest src/trials/dynamic_programming/coin_change_test.py

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=src

# Skip test data generation (if data already exists)
uv run pytest --no-cov
```

**Note**: Test data is automatically generated before running tests via `conftest.py`

### Automatic Test Data Generation

The project automatically generates test data before running tests using a pytest plugin (`src/conftest.py`). This ensures:

- **Fresh Data**: Test data is always up-to-date
- **No Manual Steps**: No need to remember to generate data
- **Consistent Results**: Same data for all test runs
- **Error Handling**: Graceful handling if generation fails

**How it works:**
1. `pytest_configure()` runs before any tests
2. Executes `testbed generate-test-data`
3. Shows success/failure messages
4. Continues with normal test execution

**Disable auto-generation** (if needed):
```bash
# Set environment variable to skip
SKIP_TEST_DATA_GENERATION=1 uv run pytest
```

### Manual Test Data Generation
```bash
# Generate all test data using CLI
uv run testbed generate-test-data

# Generate test data for a specific problem
uv run python src/trials/dynamic_programming/coin_change_test_gen.py

# Generate all test data (alternative method)
find src/trials -name "*_test_gen.py" -exec uv run python {} \;
```

## 📝 How to Add a New Problem

### 1. Create Solution File

Create `src/trials/{category}/{problem_name}.py`:

```python
"""Problem Name.

Brief description of the problem.

Example:
Input: param1 = [1, 2, 3], param2 = 5
Output: 6

"""

def solution(param1: list[int], param2: int) -> int:
    """Problem solution.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value
    """
    # Your solution here
    pass
```

### 2. Create Test Generator

Create `src/trials/{category}/{problem_name}_test_gen.py`:

```python
"""Problem Name Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig

def _basic():
    return TestCase(
        description="Basic test case",
        expected=6,
        inputs={"param1": [1, 2, 3], "param2": 5},
    )

def _edge_case():
    return TestCase(
        description="Edge case",
        expected=0,
        inputs={"param1": [], "param2": 0},
    )

def generate_test_data():
    """Generate test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic),
            TestDataGeneratorConfig(generator_function=_edge_case),
        ],
        "category/problem_name.parquet",
    )

if __name__ == "__main__":
    generate_test_data()
```

### 3. Create Test File

Create `src/trials/{category}/{problem_name}_test.py`:

```python
"""Problem Name Tests."""

import pytest
from pathlib import Path
from utils.test_data_loader import parametrize_from_file
from .problem_name import solution

@parametrize_from_file(
    file_path=Path(__file__).parent.parent.parent.parent / "data" / "category" / "problem_name.parquet",
    input_keys=["param1", "param2"],
    expected_key="expected",
    description_key="description"
)
def test_solution(param1, param2, expected, description):
    """Test solution with generated data."""
    result = solution(param1, param2)
    assert result == expected, f"Failed for {description}: expected {expected}, got {result}"
```

### 4. Generate Test Data

```bash
uv run python src/trials/{category}/{problem_name}_test_gen.py
```

### 5. Run Tests

```bash
uv run pytest src/trials/{category}/{problem_name}_test.py -v
```

## 📊 Data Management with SHA

### Data Storage Structure

Test data is stored in `data/{category}/` with the following structure:

```
data/dynamic_programming/
├── coin_change.parquet          # Test data in Parquet format
├── coin_change.sha              # SHA checksum of test generator
├── climbing_stairs.parquet      # Another problem's data
├── climbing_stairs.sha          # SHA checksum
└── ...
```

### SHA Verification

Each `.sha` file contains the SHA-256 hash of the corresponding test generator:

```
77acc727b75a4646a9a0f74959d0e70de69cbe03d09fbe276b4775eb88f43b1a  coin_change_test_gen.py
```

This ensures:
- **Data Integrity**: Test data matches the generator that created it
- **Version Control**: Changes to generators are tracked
- **Reproducibility**: Same generator produces same data

### Data Formats

#### Parquet Files (Recommended)
- **Fast I/O**: Much faster than JSON for large datasets
- **Compression**: Excellent compression for large test cases
- **Type Safety**: Maintains data types and schema
- **Column Structure**: Input parameters prefixed with `input_`

Example Parquet structure:
```
| description | input_coins | input_amount | expected |
|-------------|-------------|--------------|----------|
| Basic test  | [1,2,5]     | 11           | 3        |
| Edge case   | [4,6]       | 7            | -1       |
```

#### JSON Files (Legacy)
```json
{
  "test_cases": [
    {
      "description": "Basic test case",
      "input": {
        "coins": [1, 2, 5],
        "amount": 11
      },
      "expected": 3
    }
  ]
}
```

## 📚 Documentation

### Document Structure

Documents are organized by category and timestamp:

```
documents/dynamic_programming/
├── README.md                     # Category overview and patterns
├── 2025-09-28T18:08:00/         # Timestamped problem sets
│   ├── PROBLEMS.md              # Problem descriptions
│   └── SOLUTIONS.md             # Solution explanations
└── ...
```

### Adding Documentation

1. **Category Overview**: Update `documents/{category}/README.md`
2. **Problem Sets**: Create timestamped directories for problem batches
3. **Problem Descriptions**: Document in `PROBLEMS.md`
4. **Solution Explanations**: Document in `SOLUTIONS.md`

## 🛠️ Utilities

### Test Data Generator

The `utils.data_generator` module provides:

- `TestCase`: Individual test case definition
- `TestDataGenerator`: Main generator class
- `TestDataGeneratorConfig`: Configuration for test cases
- `generate_test_data()`: Generate and save test data

### Test Data Loader

The `utils.test_data_loader` module provides:

- `parametrize_from_file()`: Pytest decorator for loading test data
- Support for Parquet, JSON, and YAML formats
- Automatic parameter mapping
- Description support for better test output

## 🧪 Testing Best Practices

### Test Case Design

1. **Basic Cases**: Simple, obvious inputs
2. **Edge Cases**: Empty inputs, single elements, boundary values
3. **Performance Cases**: Large inputs for stress testing
4. **Corner Cases**: Unusual but valid inputs

### Test Data Organization

1. **Descriptive Names**: Clear, concise test case descriptions
2. **Grouped Cases**: Related test cases together
3. **Comments**: Explain complex expected values
4. **Consistent Format**: Follow established patterns

### Example Test Case

```python
def _large_performance():
    """Large but deterministic test case."""
    return TestCase(
        description="large canonical coins amount=10000",
        expected=400,  # 10000 // 25
        inputs={"coins": [1, 5, 10, 25], "amount": 10000},
    )
```

## 🔧 Development Workflow

### 1. Problem Development
1. Create solution file
2. Write test generator with various test cases
3. Generate test data
4. Create test file
5. Run tests to verify solution

### 2. Data Management
1. Test data is automatically generated from test generators
2. SHA files track generator integrity
3. Parquet format for performance and compression
4. Version control tracks changes

### 3. Documentation
1. Update category README for new patterns
2. Document problem sets with timestamps
3. Explain solutions and approaches
4. Maintain problem descriptions

## 📈 Performance Considerations

### Large Test Cases
- Use Parquet format for large datasets
- Generate performance test cases with `_large_perf()` functions
- Consider memory usage for very large inputs
- Use streaming for extremely large datasets

### Test Execution
- Run specific test categories during development
- Use `-v` flag for verbose output
- Profile slow tests with `--durations` flag
- Parallel execution with `-n auto` (if pytest-xdist installed)

## 🤝 Contributing

1. Follow the established file naming conventions
2. Include comprehensive test cases
3. Document your solutions clearly
4. Update relevant documentation
5. Ensure all tests pass before submitting

## 📋 File Naming Conventions

- **Solutions**: `{problem_name}.py`
- **Test Generators**: `{problem_name}_test_gen.py`
- **Test Files**: `{problem_name}_test.py`
- **Data Files**: `{problem_name}.parquet`
- **SHA Files**: `{problem_name}.sha`

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure proper module structure
2. **Data Loading**: Check file paths and formats
3. **SHA Mismatch**: Regenerate data if generator changed
4. **Performance**: Use Parquet for large datasets

### Debugging

```bash
# Run with verbose output
uv run pytest -v -s

# Run specific test with debugging
uv run pytest src/trials/dynamic_programming/coin_change_test.py::test_solution -v -s

# Check data file contents
uv run python -c "import pandas as pd; print(pd.read_parquet('data/dynamic_programming/coin_change.parquet'))"
```

---

This testbed provides a robust foundation for algorithm development and testing. The SHA-based data integrity ensures reproducible results, while the organized structure makes it easy to add new problems and maintain existing ones.
