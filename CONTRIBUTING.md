# Contributing to IBQF

Thank you for contributing to the 1-Bit Quantum Filter research project!

## How to Add Files

This repository is designed to make it easy to add your research materials:

### Adding Source Code

1. Add Python modules to `src/`
2. Follow PEP 8 style guidelines
3. Include docstrings for all functions and classes
4. Add corresponding tests to `tests/`

Example:
```bash
# Add a new module
touch src/my_module.py

# Add tests for it
touch tests/test_my_module.py
```

### Adding Data

1. Place datasets in the `data/` directory
2. For large files (>50MB), consider using Git LFS:
   ```bash
   git lfs track "*.csv"
   git lfs track "*.h5"
   ```
3. Document your data in `data/README.md`

### Adding Notebooks

1. Create Jupyter notebooks in `notebooks/`
2. Use numbered prefixes for ordering: `01_`, `02_`, etc.
3. Clear outputs before committing: `jupyter nbconvert --clear-output --inplace notebook.ipynb`

### Adding Results

1. Save figures, plots, and results to `results/`
2. Use descriptive filenames with dates if applicable
3. Consider organizing in subdirectories by experiment

### Adding Documentation

1. Add paper drafts and documentation to `docs/`
2. Use Markdown or LaTeX as appropriate
3. Keep documentation up to date with code changes

## Development Workflow

### Setting Up Your Environment

```bash
# Clone the repository
git clone https://github.com/Xenofon-Chiotopoulos/IBQF.git
cd IBQF

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

Before committing changes, make sure tests pass:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_ibqf.py -v
```

### Code Style

We follow PEP 8 style guidelines. You can check your code with:

```bash
# Install development tools
pip install black flake8

# Format code
black src/ tests/ scripts/

# Check style
flake8 src/ tests/ scripts/
```

## Git Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Add description of changes"
   ```

3. Push to GitHub:
   ```bash
   git push origin feature/my-new-feature
   ```

## Questions?

If you have questions about contributing, please open an issue on GitHub.
