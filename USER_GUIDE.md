# BoundedTest User Guide

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Theoretical Background](#theoretical-background)
4. [Package Structure](#package-structure)
5. [Detailed Usage](#detailed-usage)
6. [Examples](#examples)
7. [Interpreting Results](#interpreting-results)
8. [Comparison with MATLAB Code](#comparison-with-matlab-code)
9. [Troubleshooting](#troubleshooting)

## Installation

### From PyPI (when published)

```bash
pip install boundedtest
```

### From Source

```bash
git clone https://github.com/merwanroudane/boundedtest.git
cd boundedtest
pip install -e .
```

### Dependencies

- Python >= 3.8
- NumPy >= 1.20.0
- SciPy >= 1.7.0
- Pandas >= 1.3.0
- Statsmodels >= 0.13.0

## Quick Start

```python
import numpy as np
from boundedtest import bounded_unit_root_test

# Generate or load your bounded data
data = np.random.randn(200)  # Your time series
bounds = (-10, 10)  # Your bounds

# Run the test (recommended settings)
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    statistic='mz_alpha',
    detrending='gls_bounds',  # Use bound-specific GLS
    lrv_method='np'  # Non-parametric LRV
)

# View results
print(result)
print(f"Reject unit root hypothesis: {result.reject_5pct}")
```

## Theoretical Background

### The Model

The package implements tests for bounded processes defined as:

```
x_t = μ + y_t
y_t = α·y_{t-1} + u_t
```

where `x_t ∈ [b, b̄]` almost surely for all t, and the disturbance term contains regulators to maintain bounds.

### Test Statistics

Three M-type statistics are implemented:

1. **MZα**: Modified Phillips-Perron statistic
   - Left-tail test: Reject H₀ if MZα < critical value
   
2. **MSB**: Modified Sargan-Bhargava statistic
   - Right-tail test: Reject H₀ if MSB > critical value
   
3. **MZt**: Modified t-statistic
   - Left-tail test: Reject H₀ if MZt < critical value

### Hypotheses

- **H₀**: Series has a unit root (is I(1) and bounded)
- **H₁**: Series is stationary (is I(0) and bounded)

### Key Innovation: Bound-Specific κ̅

The GLS-detrending uses a non-centrality parameter κ̅(c,c̄) that depends on the bounds:
- Narrower bounds → more negative κ̅
- Wider bounds → κ̅ approaches -7 (standard ERS value)

## Package Structure

```
boundedtest/
├── boundedtest/
│   ├── __init__.py           # Main package interface
│   ├── core.py               # Main testing function
│   ├── statistics.py         # Test statistics computation
│   ├── detrending.py         # OLS and GLS detrending
│   ├── lrv.py                # Long-run variance estimation
│   ├── noncentrality.py      # κ̅ parameter lookup/computation
│   ├── regulated_ou.py       # Regulated OU process simulation
│   └── critical_values.py    # Critical value tables
├── examples/
│   └── example_usage.py      # Comprehensive examples
├── tests/
│   └── test_basic.py         # Unit tests
├── setup.py                  # Package configuration
├── README.md                 # Package documentation
└── LICENSE                   # MIT License

```

## Detailed Usage

### 1. Basic Testing

```python
from boundedtest import bounded_unit_root_test

result = bounded_unit_root_test(
    data=your_data,
    bounds=(lower, upper),
    statistic='mz_alpha',
    detrending='gls_bounds',
    lrv_method='np'
)
```

### 2. Choosing Detrending Method

#### OLS Detrending
```python
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    detrending='ols'  # Simple OLS
)
```

#### GLS-ERS (Standard)
```python
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    detrending='gls_ers'  # κ = -7 (ignores bounds)
)
```

#### GLS-BOUNDS (Recommended)
```python
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    detrending='gls_bounds'  # Bound-specific κ̅
)
```

### 3. Choosing Test Statistic

```python
# Single statistic
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    statistic='mz_alpha'  # or 'msb', 'mz_t'
)

# All statistics
results_dict = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    statistic='all'  # Returns dictionary
)
```

### 4. LRV Estimation Methods

#### Non-parametric (Recommended)
```python
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    lrv_method='np'  # Newey-West with automatic bandwidth
)
```

#### Parametric (AR-based)
```python
result = bounded_unit_root_test(
    data=data,
    bounds=bounds,
    lrv_method='ar'  # AR with MAIC lag selection
)
```

### 5. Working with Pandas

```python
import pandas as pd

# From DataFrame column
df = pd.DataFrame({'series': your_data})
result = bounded_unit_root_test(
    data=df['series'],
    bounds=bounds
)

# From Series
series = pd.Series(your_data)
result = bounded_unit_root_test(
    data=series,
    bounds=bounds
)
```

## Examples

### Example 1: Unemployment Rate

```python
import numpy as np
from boundedtest import bounded_unit_root_test

# Unemployment rate (bounded 0-100%)
unemployment = your_unemployment_data

result = bounded_unit_root_test(
    data=unemployment,
    bounds=(0, 100),
    detrending='gls_bounds'
)

print(f"Test Statistic: {result.statistic:.4f}")
print(f"Reject H0: {result.reject_5pct}")
```

### Example 2: Comparing Detrending Methods

```python
methods = ['ols', 'gls_ers', 'gls_bounds']
results = {}

for method in methods:
    results[method] = bounded_unit_root_test(
        data=your_data,
        bounds=bounds,
        detrending=method
    )
    
# Compare
for method, result in results.items():
    print(f"{method}: MZα={result.statistic:.4f}, "
          f"Reject={result.reject_5pct}")
```

### Example 3: Monte Carlo Simulation

```python
from boundedtest.regulated_ou import generate_bounded_ar1
import numpy as np

# Simulate under H0
n_sim = 1000
rejections = 0

for i in range(n_sim):
    data = generate_bounded_ar1(
        T=200,
        bounds=(-5, 5),
        rho=1.0,  # Unit root
        sigma=1.0,
        seed=i
    )
    
    result = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        detrending='gls_bounds'
    )
    
    if result.reject_5pct:
        rejections += 1

size = rejections / n_sim
print(f"Empirical size (5% level): {size:.3f}")
```

## Interpreting Results

### Result Object Attributes

```python
result.statistic           # Test statistic value
result.statistic_name      # Name of statistic
result.critical_values     # Dict with 10%, 5%, 1% critical values
result.reject_5pct         # Boolean: Reject at 5%?
result.pvalue              # P-value (if available)
result.bounds              # (lower, upper) bounds used
result.c_parameters        # (c_lower, c_upper) estimated
result.kappa               # κ̅ parameter (for GLS)
result.lrv_estimate        # Estimated LRV
result.sample_size         # Sample size T
result.detrending_method   # Detrending used
result.lrv_method          # LRV method used
```

### Decision Rules

For **MZα** and **MZt** (left-tail tests):
- If statistic < critical value → Reject H₀
- Smaller (more negative) values provide more evidence against H₀

For **MSB** (right-tail test):
- If statistic > critical value → Reject H₀
- Larger values provide more evidence against H₀

### Understanding c-parameters

The c-parameters (c, c̄) standardize the bounds:
```
c = (b - ŷ₁) / (σ√T)
c̄ = (b̄ - ŷ₁) / (σ√T)
```

- Narrower bounds → smaller |c| and |c̄|
- These determine the appropriate κ̅ value

## Comparison with MATLAB Code

This Python implementation is designed to be compatible with the original MATLAB code:

### Key Compatibilities

1. **Algorithm**: Follows paper exactly
2. **Detrending**: Same GLS quasi-differencing
3. **LRV**: Same NP and AR methods
4. **Iterative procedure**: Same 2-step estimation
5. **Critical values**: Based on same simulations

### Verification

The package includes verification tests showing results match expected values from the paper's Monte Carlo experiments.

## Troubleshooting

### Common Issues

**Issue**: "Data contains values outside specified bounds"
**Solution**: Check that bounds correctly encompass your data. Adjust bounds or clip data.

```python
data = np.clip(data, lower_bound, upper_bound)
```

**Issue**: Test statistic is NaN
**Solution**: Check for insufficient data or numerical issues. Ensure T > 30.

**Issue**: All tests fail to reject
**Solution**: Data might truly have unit root. Try:
- Different detrending methods
- Check if bounds are too wide
- Verify data quality

### Getting Help

1. Check examples in `examples/example_usage.py`
2. Run verification: `python verify_installation.py`
3. View test cases in `tests/test_basic.py`
4. Contact: merwanroudane920@gmail.com

## Advanced Topics

### Custom Critical Values

```python
from boundedtest.regulated_ou import compute_critical_values

cv = compute_critical_values(
    c_lower=-0.5,
    c_upper=0.5,
    kappa=0,
    n_sim=10000,
    alpha=0.05
)
```

### Custom κ̅ Computation

```python
from boundedtest.noncentrality import compute_kappa_table

kappa_table = compute_kappa_table(
    c_values=np.arange(0.1, 1.1, 0.1),
    T=1000,
    n_sim=10000
)
```

### Manual Component Usage

```python
from boundedtest import (
    ols_detrend,
    gls_detrend,
    estimate_lrv_np,
    compute_mz_alpha
)

# Manual workflow
y_tilde, _, _ = ols_detrend(data)
from boundedtest.statistics import compute_ar1_residuals
residuals = compute_ar1_residuals(y_tilde)
s2 = estimate_lrv_np(residuals)
mz_alpha = compute_mz_alpha(y_tilde, s2)
```

## References

1. Carrion-i-Silvestre, J.L. and Gadea, M.D. (2013). "GLS-based unit root tests for bounded processes." *Economics Letters*, 120(2), 184-187.

2. Elliott, G., Rothenberg, T.J., and Stock, J.H. (1996). "Efficient Tests for an Autoregressive Unit Root." *Econometrica*, 64(4), 813-836.

3. Ng, S. and Perron, P. (2001). "Lag Length Selection and the Construction of Unit Root Tests with Good Size and Power." *Econometrica*, 69(6), 1519-1554.

4. Cavaliere, G. (2005). "Limited time series with a unit root." *Econometric Theory*, 21(5), 907-945.

## Citation

When using this package, please cite:

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

**Author**: Merwan Roudane  
**Email**: merwanroudane920@gmail.com  
**GitHub**: [@merwanroudane](https://github.com/merwanroudane)
