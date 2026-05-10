# Test Generation Reference

## Testing Best Practices

### Test Naming Conventions

**Pattern:** `test_<function>_<scenario>_<expected_result>`

Examples:
- `test_calculate_total_with_valid_items_returns_sum()`
- `test_validate_email_with_invalid_format_raises_error()`
- `test_get_user_when_not_found_returns_none()`

### Test Organization

```
tests/
├── unit/              # Fast, isolated tests
│   ├── test_utils.py
│   └── test_models.py
├── integration/       # Tests with dependencies
│   ├── test_api.py
│   └── test_database.py
└── e2e/              # End-to-end tests
    └── test_workflows.py
```

### Test Coverage Goals

- **Critical paths:** 100% coverage
- **Business logic:** 90%+ coverage
- **Utilities:** 80%+ coverage
- **UI components:** 70%+ coverage

## AAA Pattern Explained

### Arrange
Set up the test environment:
```python
# Create test data
user = User(name="John", email="john@example.com")
mock_db = MockDatabase()
service = UserService(mock_db)
```

### Act
Execute the code being tested:
```python
# Call the function
result = service.create_user(user)
```

### Assert
Verify the outcome:
```python
# Check expectations
assert result.id is not None
assert result.name == "John"
assert mock_db.save_called == True
```

## Common Testing Patterns

### 1. Parameterized Tests
Test multiple inputs efficiently:
```python
@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 1),
    (5, 120),  # 5! = 120
])
def test_factorial(input, expected):
    assert factorial(input) == expected
```

### 2. Fixtures
Reuse test setup:
```python
@pytest.fixture
def sample_user():
    return User(name="Test", email="test@example.com")

def test_user_creation(sample_user):
    assert sample_user.name == "Test"
```

### 3. Mocking
Isolate code from dependencies:
```python
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {'status': 'ok'}
    result = fetch_data()
    assert result['status'] == 'ok'
```

### 4. Exception Testing
Verify error handling:
```python
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

## Test Quality Checklist

- [ ] Tests are independent (can run in any order)
- [ ] Tests are fast (< 100ms for unit tests)
- [ ] Tests are deterministic (same result every time)
- [ ] Tests have clear, descriptive names
- [ ] Tests follow AAA pattern
- [ ] Tests cover edge cases
- [ ] Tests verify one thing at a time
- [ ] Tests use appropriate assertions
- [ ] Tests clean up after themselves
- [ ] Tests are maintainable (not brittle)

## Edge Cases to Consider

### Numeric Inputs
- Zero
- Negative numbers
- Very large numbers
- Floating point precision
- Infinity, NaN

### String Inputs
- Empty string
- Very long strings
- Special characters
- Unicode characters
- Whitespace only

### Collections
- Empty arrays/lists
- Single item
- Duplicate items
- Null items
- Very large collections

### Dates/Times
- Past dates
- Future dates
- Leap years
- Time zones
- Daylight saving time

### Null/Undefined
- Null parameters
- Undefined values
- Missing optional parameters
