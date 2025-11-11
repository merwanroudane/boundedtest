# Package Configuration Files - Overview

## Configuration Files in boundedtest

The package now includes both modern and traditional Python packaging configurations:

---

## 📄 pyproject.toml (NEW! ✨)

**Purpose**: Modern Python packaging configuration (PEP 517/518)

**What it contains**:
- ✅ Package metadata (name, version, author, description)
- ✅ Dependencies (numpy, scipy, pandas, statsmodels)
- ✅ Development dependencies (pytest, black, flake8, mypy)
- ✅ Build system requirements
- ✅ Tool configurations (black, pytest, mypy, coverage)
- ✅ Project URLs (GitHub, documentation)
- ✅ Package classifiers

**Why use it**:
- Modern Python packaging standard (Python 3.7+)
- Single source of truth for package configuration
- Better integration with modern tools
- Cleaner and more maintainable
- Future-proof

**Installation**:
```bash
pip install -e .
```

---

## 📄 setup.py

**Purpose**: Traditional Python packaging (setuptools)

**What it contains**:
- ✅ Package metadata
- ✅ Dependencies
- ✅ Installation configuration
- ✅ Package discovery

**Why it's included**:
- Maximum compatibility
- Works with older pip versions
- Familiar to many users
- Fallback option

**Installation**:
```bash
python setup.py develop
# or
pip install -e .
```

---

## 📄 requirements.txt

**Purpose**: Simple dependency listing

**What it contains**:
```
numpy>=1.20.0
scipy>=1.7.0
pandas>=1.3.0
statsmodels>=0.13.0
```

**Why use it**:
- Quick dependency installation
- CI/CD pipelines
- Docker containers
- Simple and straightforward

**Installation**:
```bash
pip install -r requirements.txt
```

---

## 📄 MANIFEST.in

**Purpose**: Specifies additional files to include in distribution

**What it contains**:
```
include README.md
include LICENSE
include setup.py
recursive-include boundedtest *.py
recursive-include examples *.py
recursive-include tests *.py
```

**Why it's needed**:
- Ensures documentation is included in package
- Includes examples and tests
- Required for source distributions

---

## 📄 .gitignore

**Purpose**: Specifies files Git should ignore

**What it contains**:
- Python cache files (`__pycache__`, `*.pyc`)
- Build directories (`build/`, `dist/`, `*.egg-info/`)
- Virtual environments (`venv/`, `env/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`)

**Why it's needed**:
- Keeps repository clean
- Prevents committing generated files
- Standard for Python projects

---

## Comparison: pyproject.toml vs setup.py

| Feature | pyproject.toml | setup.py |
|---------|---------------|----------|
| **Standard** | PEP 517/518 (modern) | setuptools (traditional) |
| **Python Version** | 3.7+ | All versions |
| **Format** | TOML | Python |
| **Tool Config** | ✅ Integrated | ❌ Separate files |
| **Future-proof** | ✅ Yes | ⚠️ Maintained |
| **Learning Curve** | Easy (declarative) | Medium (code) |
| **Our Package** | ✅ Primary | ✅ Fallback |

---

## Which One Should You Use?

### Use pyproject.toml if:
- ✅ Using Python 3.7 or later
- ✅ Want modern packaging
- ✅ Using tools like black, pytest, mypy
- ✅ Starting a new project
- ✅ Want a single configuration file

### Use setup.py if:
- ✅ Need compatibility with older pip
- ✅ Prefer traditional approach
- ✅ Have existing setup.py workflow
- ✅ Need custom build logic

### Our Package: Both Work! 🎉

The boundedtest package includes both configurations, so you can use either one:

```bash
# Both of these work identically:
pip install -e .
python setup.py develop
```

---

## Installation Examples

### Standard Installation (uses pyproject.toml)
```bash
cd boundedtest
pip install -e .
```

### With Development Dependencies
```bash
cd boundedtest
pip install -e ".[dev]"
```

### Traditional Installation
```bash
cd boundedtest
python setup.py develop
```

### Just Dependencies
```bash
cd boundedtest
pip install -r requirements.txt
```

---

## Tool Configurations in pyproject.toml

### Black (Code Formatter)
```toml
[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310', 'py311']
```

Usage: `black boundedtest/`

### Pytest (Testing)
```toml
[tool.pytest.ini_options]
minversion = "6.0"
testpaths = ["tests"]
```

Usage: `pytest tests/`

### MyPy (Type Checking)
```toml
[tool.mypy]
python_version = "3.8"
ignore_missing_imports = true
```

Usage: `mypy boundedtest/`

### Coverage (Test Coverage)
```toml
[tool.coverage.run]
source = ["boundedtest"]
```

Usage: `pytest --cov=boundedtest tests/`

---

## File Structure Summary

```
boundedtest/
├── pyproject.toml          ← Modern config (PRIMARY)
├── setup.py                ← Traditional config (FALLBACK)
├── requirements.txt        ← Simple dependencies
├── MANIFEST.in             ← Distribution files
├── .gitignore              ← Git exclusions
├── LICENSE                 ← MIT License
├── README.md               ← Main docs
├── INSTALLATION_GUIDE.md   ← This overview
└── boundedtest/            ← Package code
    └── ...
```

---

## Quick Reference

### Install Package
```bash
pip install -e .
```

### Install with Dev Tools
```bash
pip install -e ".[dev]"
```

### Run Tests
```bash
pytest tests/
```

### Format Code
```bash
black boundedtest/
```

### Check Types
```bash
mypy boundedtest/
```

### Build Distribution
```bash
python -m build
```

---

## Metadata Comparison

Both configurations contain the same package information:

**Package Name**: boundedtest  
**Version**: 1.0.0  
**Author**: Merwan Roudane  
**Email**: merwanroudane920@gmail.com  
**License**: MIT  
**Python**: ≥3.8  

**Dependencies**:
- numpy ≥ 1.20.0
- scipy ≥ 1.7.0
- pandas ≥ 1.3.0
- statsmodels ≥ 0.13.0

---

## Building and Publishing

### Build Package (modern)
```bash
python -m build
```

Creates:
- `dist/boundedtest-1.0.0.tar.gz`
- `dist/boundedtest-1.0.0-py3-none-any.whl`

### Build Package (traditional)
```bash
python setup.py sdist bdist_wheel
```

### Publish to PyPI
```bash
twine upload dist/*
```

---

## Troubleshooting

### "No module named 'build'"
```bash
pip install build
```

### "pyproject.toml not found"
The file is at the root of the package, same level as setup.py

### "Which file is being used?"
When you run `pip install -e .`, pip will:
1. First look for `pyproject.toml`
2. Fall back to `setup.py` if needed
3. Both are included for maximum compatibility

---

## Summary

✅ **pyproject.toml** - Modern, recommended, includes tool configs  
✅ **setup.py** - Traditional, compatible, fallback option  
✅ **requirements.txt** - Simple dependency list  
✅ **MANIFEST.in** - Distribution file inclusion  
✅ **.gitignore** - Git exclusions  

**All work together to provide a complete, modern Python package!**

---

**Author**: Dr. Merwan Roudane  
**Email**: merwanroudane920@gmail.com  
**GitHub**: https://github.com/merwanroudane/boundedtest
