# Tests

This directory contains unit tests and integration tests for the IBQF implementation.

## Contents

- Unit tests for core functions
- Integration tests
- Test data (small samples)

## Running Tests

```bash
# Using pytest
pip install pytest
pytest

# Using unittest
python -m unittest discover tests
```

## Naming Convention

- Test files should start with `test_`, e.g., `test_ibqf.py`
- Test functions should start with `test_`, e.g., `test_filter_accuracy()`
