---
name: test-generator
description: Generate comprehensive unit and integration tests for code
tags: [testing, unit-tests, integration-tests, tdd]
---

# Test Generation Process

Follow these steps to generate comprehensive tests:

## 1. Analyze the Code

First, understand what needs to be tested:
- Identify all public functions/methods
- Determine input parameters and return types
- Note any dependencies or side effects
- Consider edge cases and error conditions

## 2. Load Testing Guidelines

Read the testing standards:
- Load `reference.md` for testing best practices
- Load `examples.md` to see test examples for different scenarios

## 3. Generate Test Cases

For each function, create tests for:

### Happy Path
- Valid inputs with expected outputs
- Common use cases
- Default parameter values

### Edge Cases
- Boundary values (min, max, zero, empty)
- Null/undefined inputs
- Special characters or formats

### Error Cases
- Invalid inputs
- Missing required parameters
- Type mismatches
- Out-of-range values

## 4. Use Test Templates

Generate tests using the appropriate template:
```bash
python scripts/generate_tests.py <source_file> <test_framework>
```

Supported frameworks:
- `pytest` (Python)
- `jest` (JavaScript/TypeScript)
- `junit` (Java)
- `rspec` (Ruby)

## 5. Structure Your Tests

Follow the AAA pattern:
- **Arrange**: Set up test data and dependencies
- **Act**: Execute the function being tested
- **Assert**: Verify the expected outcome

## 6. Add Test Documentation

Include:
- Test description explaining what is being tested
- Why the test is important
- Any setup or teardown requirements
- Expected behavior
