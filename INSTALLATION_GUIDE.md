# Installation Guide - Updated

## Overview

The **boundedtest** package now includes both modern (`pyproject.toml`) and traditional (`setup.py`) installation configurations for maximum compatibility.

---

## Installation Methods

### Method 1: Using pip (Recommended)

The simplest method - works with both `pyproject.toml` and `setup.py`:

```bash
# Extract the package
tar -xzf boundedtest.tar.gz
cd boundedtest

# Install in editable mode (recommended for development)
pip install -e .

# Or install normally
pip install .
```

### Method 2: Using build (Modern Approach)

For Python 3.7+ with `pyproject.toml`:

```bash
# Install build tools
pip install build

# Build the package
python -m build

# Install from the built wheel
pip install dist/boundedtest-1.0.0-py3-none-any.whl
```

### Method 3: Using setup.py (Traditional)

Still supported for compatibility:

```bash
python setup.py develop  # Development mode
# or
python setup.py install  # Standard installation
```

---

## What's Included

### Configuration Files

**pyproject.toml** (Modern - PEP 517/518)
- Modern Python packaging standard
- Includes all metadata and dependencies
- Better tool configuration (black, pytest, mypy)
- Recommended for new projects

**setup.py** (Traditional - setuptools)
- Classic Python packaging
- Maximum compatibility
- Works with older pip versions
- Fallback option

Both files are equivalent and either can be used!

---

## Verify Installation

After installation, verify it works:

```bash
# Quick check
python -c "import boundedtest; print('Success!')"

# Full verification
python verify_installation.py
```

Expected output:
```
======================================================================
BOUNDEDTEST PACKAGE VERIFICATION
======================================================================

1. Importing package...
   ✓ Package imported successfully

[... all tests should pass ...]

ALL TESTS PASSED SUCCESSFULLY! ✓
```

---

## Installation with Different Tools

### Using pip (any version)
```bash
pip install -e .
```

### Using pip 21.3+ (with pyproject.toml)
```bash
pip install -e .
```

### Using conda
```bash
# Install dependencies first
conda install numpy scipy pandas statsmodels

# Then install package
pip install -e .
```

### Using poetry
```bash
# If you want to use poetry
poetry install
```

---

## Dependencies

The package requires:

- **Python** ≥ 3.8
- **NumPy** ≥ 1.20.0
- **SciPy** ≥ 1.7.0
- **Pandas** ≥ 1.3.0
- **Statsmodels** ≥ 0.13.0

Optional (for development):
- pytest ≥ 6.0
- pytest-cov ≥ 2.0
- black ≥ 22.0
- flake8 ≥ 4.0
- mypy ≥ 0.950

---

## Installing Development Dependencies

### Using pip with pyproject.toml
```bash
pip install -e ".[dev]"
```

This installs the package plus development tools (pytest, black, etc.)

### Manual installation
```bash
pip install pytest pytest-cov black flake8 mypy
```

---

## Virtual Environment (Recommended)

### Create virtual environment

**On Linux/Mac:**
```bash
python -m venv boundedtest_env
source boundedtest_env/bin/activate
cd boundedtest
pip install -e .
```

**On Windows:**
```bash
python -m venv boundedtest_env
boundedtest_env\Scripts\activate
cd boundedtest
pip install -e .
```

### With conda
```bash
conda create -n boundedtest python=3.10
conda activate boundedtest
cd boundedtest
pip install -e .
```

---

## Troubleshooting

### Issue: "No module named 'setuptools'"
```bash
pip install --upgrade setuptools wheel
```

### Issue: "No module named 'build'"
```bash
pip install build
```

### Issue: Permission denied
```bash
# Use --user flag
pip install --user -e .

# Or use virtual environment (recommended)
python -m venv env
source env/bin/activate  # Linux/Mac
# env\Scripts\activate  # Windows
pip install -e .
```

### Issue: Dependencies not installing
```bash
# Install dependencies manually first
pip install numpy scipy pandas statsmodels

# Then install package
pip install -e .
```

---

## Uninstallation

To uninstall the package:

```bash
pip uninstall boundedtest
```

---

## Building Distribution Files

If you want to create distribution files for PyPI:

### Using build (modern)
```bash
pip install build twine
python -m build
```

This creates:
- `dist/boundedtest-1.0.0.tar.gz` (source distribution)
- `dist/boundedtest-1.0.0-py3-none-any.whl` (wheel)

### Using setup.py (traditional)
```bash
python setup.py sdist bdist_wheel
```

### Upload to PyPI
```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Then real PyPI
twine upload dist/*
```

---

## Installation from PyPI (After Publishing)

Once published, anyone can install with:

```bash
pip install boundedtest
```

---

## Checking Package Information

After installation:

```bash
# Check version
python -c "import boundedtest; print(boundedtest.__version__)"

# Check location
pip show boundedtest

# List package files
pip show -f boundedtest
```

---

## Development Setup

For package development:

```bash
# Clone/extract package
cd boundedtest

# Create virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black boundedtest/

# Type check
mypy boundedtest/

# Lint
flake8 boundedtest/
```

---

## System Requirements

### Operating Systems
- ✅ Linux (tested)
- ✅ macOS (should work)
- ✅ Windows (should work)

### Python Versions
- ✅ Python 3.8
- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11
- ✅ Python 3.12

---

## Quick Installation Summary

**Most users should use:**
```bash
tar -xzf boundedtest.tar.gz
cd boundedtest
pip install -e .
python verify_installation.py
```

**That's it!** 🎉

---

## Support

If you encounter installation issues:

1. Check you have Python 3.8+: `python --version`
2. Update pip: `pip install --upgrade pip`
3. Try in a fresh virtual environment
4. Check the troubleshooting section above
5. Contact: merwanroudane920@gmail.com

---

## What's New with pyproject.toml

The addition of `pyproject.toml` provides:

✅ **Modern Python packaging standard** (PEP 517/518)  
✅ **Better dependency management**  
✅ **Integrated tool configuration** (black, pytest, mypy)  
✅ **Cleaner build process**  
✅ **Future-proof packaging**  

You can still use `setup.py` if you prefer - both work perfectly!

---

**Author**: Dr. Merwan Roudane  
**Email**: merwanroudane920@gmail.com  
**GitHub**: https://github.com/merwanroudane/boundedtest
