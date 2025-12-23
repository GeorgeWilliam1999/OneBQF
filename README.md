# IBQF - 1-Bit Quantum Filter for Particle Track Reconstruction

This repository accompanies the paper on the 1-Bit Quantum Filter (IBQF) for particle track reconstruction.

## Repository Structure

```
IBQF/
├── src/              # Source code implementation
├── data/             # Datasets and input files
├── notebooks/        # Jupyter notebooks for experiments
├── results/          # Experimental results and figures
├── docs/             # Documentation and paper materials
├── tests/            # Unit and integration tests
├── scripts/          # Utility scripts
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Xenofon-Chiotopoulos/IBQF.git
cd IBQF
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Code

Add your IBQF implementation to the `src/` directory and import it:

```python
from src.ibqf import IBQF

# Your code here
```

### Running Experiments

1. Add your datasets to the `data/` directory
2. Create experiment notebooks in `notebooks/`
3. Run utility scripts from `scripts/`
4. Save results to `results/`

### Running Tests

```bash
pytest tests/
```

## Adding Files to This Repository

This repository is organized to make it easy to add your research materials:

1. **Code**: Add implementation files to `src/`
2. **Data**: Place datasets in `data/` (use Git LFS for large files)
3. **Notebooks**: Add Jupyter notebooks to `notebooks/`
4. **Results**: Save figures and results to `results/`
5. **Documentation**: Add paper drafts and docs to `docs/`
6. **Tests**: Add test files to `tests/`
7. **Scripts**: Add utility scripts to `scripts/`

Each directory contains a README.md with specific guidance.

## Contributing

Feel free to add your own modules, experiments, and documentation as the research progresses.

## Citation

If you use this code in your research, please cite:

```bibtex
@article{IBQF2024,
  title={1-Bit Quantum Filter for Particle Track Reconstruction},
  author={Your Name},
  journal={Journal Name},
  year={2024}
}
```

## License

See [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on GitHub.
