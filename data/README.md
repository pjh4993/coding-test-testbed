# Test Data Management

This directory contains test data files for managing test cases externally, making it easier to manage large test cases and complex expected values.

## Structure

```
data/
├── sorting_searching/
│   ├── kth_largest_element.json
│   ├── kth_largest_element.yaml
│   └── search_in_rotated_sorted.json
├── hashing_and_data_structures/
│   └── two_sum.json
└── dynamic_programming/
    └── (future test files)
```

## File Formats

### JSON Format
```json
{
  "test_cases": [
    {
      "description": "Test case description",
      "input": {
        "param1": "value1",
        "param2": "value2"
      },
      "expected": "expected_result"
    }
  ]
}
```

### YAML Format
```yaml
test_cases:
  - description: "Test case description"
    input:
      param1: "value1"
      param2: "value2"
    expected: "expected_result"
```

### Parquet Format
Parquet files use a tabular structure with columns:
- `description`: Test case description
- `input_param1`, `input_param2`, etc.: Input parameters (prefixed with `input_`)
- `expected`: Expected result

Example Parquet structure:
```
| description | input_nums | input_k | expected |
|-------------|-------------|---------|----------|
| Basic test  | [3,2,1,5,6] | 2       | 5        |
| Large test  | [1,2,3...]  | 50      | 51       |
```

## Usage in Tests

### Basic Usage
```python
from test_data_loader import parametrize_from_file
from pathlib import Path

@parametrize_from_file(
    file_path=Path(__file__).parent.parent / "test_data" / "category" / "problem.json",
    input_keys=["param1", "param2"],
    expected_key="expected"
)
def test_function(param1, param2, expected):
    # Your test logic here
    pass
```

### With Descriptions
```python
@parametrize_from_file(
    file_path=Path(__file__).parent.parent / "test_data" / "category" / "problem.json",
    input_keys=["param1", "param2"],
    expected_key="expected",
    description_key="description"
)
def test_function(param1, param2, expected, description):
    # Your test logic here
    print(f"Running test: {description}")
    pass
```

## Benefits

1. **Separation of Concerns**: Test data is separated from test logic
2. **Maintainability**: Easy to add/modify test cases without touching code
3. **Reusability**: Test data can be shared across different test files
4. **Scalability**: Handle large test cases with complex data structures
5. **Version Control**: Better diff tracking for test data changes
6. **Multiple Formats**: Support for JSON, YAML, and Parquet
7. **Performance Testing**: Easy to add large datasets for performance tests
8. **Compression**: Parquet files offer excellent compression for large datasets
9. **Type Safety**: Parquet maintains data types and schema information
10. **Fast I/O**: Parquet files load much faster than JSON for large datasets

## Adding New Test Cases

### For JSON/YAML Files
1. Create or edit the appropriate JSON/YAML file in the relevant category directory
2. Follow the format specified above
3. Add descriptive names and comments for complex test cases
4. Run your tests to verify the new cases work correctly

### For Parquet Files
1. **Convert existing JSON/YAML**: Use `convert_json_to_parquet()` function
2. **Generate large datasets**: Use `generate_large_test_data.py` script
3. **Create manually**: Use `create_parquet_test_data()` function
4. **Column naming**: Input parameters should be prefixed with `input_` (e.g., `input_nums`, `input_k`)

### Converting to Parquet
```python
from test_data_loader import convert_json_to_parquet

# Convert JSON to Parquet
convert_json_to_parquet(
    "test_data/sorting_searching/kth_largest_element.json",
    "test_data/sorting_searching/kth_largest_element.parquet"
)
```

### Generating Large Test Data
```bash
# Generate large performance test datasets
python src/generate_large_test_data.py

# Convert all existing JSON files to Parquet
python src/convert_to_parquet.py
```

## Best Practices

1. Use descriptive names for test cases
2. Group related test cases together
3. Include edge cases and performance tests
4. Add comments for complex expected values
5. Keep test data files organized by problem category
6. Use consistent naming conventions
