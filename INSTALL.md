# Installation and Setup Instructions

## Overview

This document provides step-by-step instructions for installing and setting up the **boundedtest** Python package.

---

## Prerequisites

### Required Software

- **Python**: Version 3.8 or higher
- **pip**: Python package installer

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If you need to install Python, visit: https://www.python.org/downloads/

---

## Installation Methods

### Method 1: Install from PyPI (Recommended when published)

Once the package is published to PyPI:

```bash
pip install boundedtest
```

### Method 2: Install from Source (Current Method)

#### Step 1: Download or Clone the Package

Option A - If you have the package folder:
```bash
cd /path/to/boundedtest
```

Option B - Clone from GitHub:
```bash
git clone https://github.com/merwanroudane/boundedtest.git
cd boundedtest
```

#### Step 2: Install the Package

For regular installation:
```bash
pip install .
```

For development installation (editable mode):
```bash
pip install -e .
```

---

## Verify Installation

### Quick Test

Create a file `test_install.py` with:

```python
import numpy as np
from boundedtest import bounded_unit_root_test

# Generate test data
np.random.seed(42)
data = np.random.randn(100)

# Run test
result = bounded_unit_root_test(
    data=data,
    bounds=(-10, 10),
    detrending='gls_bounds'
)

print("Installation successful!")
print(f"Test statistic: {result.statistic:.4f}")
```

Run it:
```bash
python test_install.py
```

### Run Verification Script

The package includes a comprehensive verification script:

```bash
cd boundedtest  # Navigate to package directory
python verify_installation.py
```

This will run multiple tests to ensure all components work correctly.

---

## Usage Examples

### Basic Example

```python
import numpy as np
from boundedtest import bounded_unit_root_test

# Your data
data = np.array([...])  # Your time series
bounds = (-5, 5)  # Your bounds

# Run test
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    statistic='mz_alpha',
    detrending='gls_bounds',
    lrv_method='np'
)

# View results
print(result)
```

### Running Examples

The package includes comprehensive examples:

```bash
cd boundedtest/examples
python example_usage.py
```

This will run 7 different examples demonstrating various features of the package.

---

## Troubleshooting

### Issue: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'boundedtest'`

**Solutions**:
1. Make sure you installed the package: `pip install .`
2. Check if you're in the correct environment (if using virtual environments)
3. Try: `pip install -e .` for editable installation

### Issue: Import Errors for Dependencies

**Error**: `ModuleNotFoundError: No module named 'numpy'` (or scipy, pandas, etc.)

**Solution**:
```bash
pip install numpy scipy pandas statsmodels
```

Or install all dependencies at once:
```bash
pip install -r requirements.txt
```

### Issue: Permission Denied

**Error**: `PermissionError` or `Permission denied`

**Solutions**:
1. Use `--user` flag: `pip install --user .`
2. Use virtual environment (recommended)
3. Use `sudo` (not recommended): `sudo pip install .`

---

## Using Virtual Environments (Recommended)

### Why Use Virtual Environments?

- Isolates package dependencies
- Prevents conflicts with system packages
- Easier to manage different project requirements

### Create and Activate Virtual Environment

#### On Linux/Mac:
```bash
# Create virtual environment
python -m venv boundedtest_env

# Activate
source boundedtest_env/bin/activate

# Install package
cd boundedtest
pip install -e .
```

#### On Windows:
```bash
# Create virtual environment
python -m venv boundedtest_env

# Activate
boundedtest_env\Scripts\activate

# Install package
cd boundedtest
pip install -e .
```

### Deactivate Virtual Environment

```bash
deactivate
```

---

## Directory Structure After Installation

```
boundedtest/
├── boundedtest/              # Main package directory
│   ├── __init__.py
│   ├── core.py
│   ├── statistics.py
│   ├── detrending.py
│   ├── lrv.py
│   ├── noncentrality.py
│   ├── regulated_ou.py
│   └── critical_values.py
├── examples/                 # Example scripts
│   └── example_usage.py
├── tests/                    # Test files
│   └── test_basic.py
├── setup.py                  # Installation configuration
├── README.md                 # Main documentation
├── USER_GUIDE.md            # Detailed user guide
├── LICENSE                   # MIT License
├── verify_installation.py   # Verification script
└── requirements.txt         # Dependencies (if present)
```

---

## Next Steps

1. ✅ **Read the User Guide**: See `USER_GUIDE.md` for comprehensive documentation

2. ✅ **Run Examples**: Try `examples/example_usage.py` to see the package in action

3. ✅ **Read the Paper**: Familiarize yourself with Carrion-i-Silvestre and Gadea (2013)

4. ✅ **Start Testing**: Apply the tests to your own data

---

## Package Information

- **Author**: Merwan Roudane
- **Email**: merwanroudane920@gmail.com
- **GitHub**: https://github.com/merwanroudane/boundedtest
- **License**: MIT
- **Python Version**: ≥ 3.8

---

## Getting Help

If you encounter any issues:

1. Check the **USER_GUIDE.md** for detailed documentation
2. Review the **examples/** directory for usage examples
3. Run the test suite: `pytest tests/` (requires pytest)
4. Contact the author: merwanroudane920@gmail.com

---

## Citation

When using this package in research, please cite:

```bibtex
@article{carrion2013gls,
  title={GLS-based unit root tests for bounded processes},
  author={Carrion-i-Silvestre, Josep Llu{\'\i}s and Gadea, Mar{\'\i}a Dolores},
  journal={Economics Letters},
  volume={120},
  number={2},
  pages={184--187},
  year={2013},
  publisher={Elsevier}
}
```

---

**Happy Testing! 🎉**
