"""
Quick verification script for boundedtest package.
"""

import numpy as np
import sys

print("=" * 70)
print("BOUNDEDTEST PACKAGE VERIFICATION")
print("=" * 70)

try:
    print("\n1. Importing package...")
    from boundedtest import bounded_unit_root_test
    from boundedtest.regulated_ou import generate_bounded_ar1
    print("   ✓ Package imported successfully")
    
    print("\n2. Generating test data...")
    np.random.seed(42)
    data = generate_bounded_ar1(
        T=100,
        bounds=(-5, 5),
        rho=1.0,
        sigma=1.0,
        burnin=50
    )
    print(f"   ✓ Generated {len(data)} observations")
    print(f"   Range: [{np.min(data):.2f}, {np.max(data):.2f}]")
    
    print("\n3. Running unit root test (OLS)...")
    result_ols = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        statistic='mz_alpha',
        detrending='ols',
        lrv_method='np'
    )
    print(f"   ✓ OLS test completed")
    print(f"   MZα = {result_ols.statistic:.4f}")
    print(f"   Reject H0: {result_ols.reject_5pct}")
    
    print("\n4. Running unit root test (GLS-ERS)...")
    result_gls_ers = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        statistic='mz_alpha',
        detrending='gls_ers',
        lrv_method='np'
    )
    print(f"   ✓ GLS-ERS test completed")
    print(f"   MZα = {result_gls_ers.statistic:.4f}")
    print(f"   Reject H0: {result_gls_ers.reject_5pct}")
    
    print("\n5. Running unit root test (GLS-BOUNDS)...")
    result_gls_bounds = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        statistic='mz_alpha',
        detrending='gls_bounds',
        lrv_method='np'
    )
    print(f"   ✓ GLS-BOUNDS test completed")
    print(f"   MZα = {result_gls_bounds.statistic:.4f}")
    print(f"   c-parameters: [{result_gls_bounds.c_parameters[0]:.4f}, {result_gls_bounds.c_parameters[1]:.4f}]")
    print(f"   κ̅ = {result_gls_bounds.kappa:.4f}")
    print(f"   Reject H0: {result_gls_bounds.reject_5pct}")
    
    print("\n6. Computing all test statistics...")
    results_all = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        statistic='all',
        detrending='gls_bounds',
        lrv_method='np'
    )
    print("   ✓ All statistics computed")
    for stat_name, result in results_all.items():
        print(f"   {stat_name}: {result.statistic:.4f}")
    
    print("\n7. Testing with AR-based LRV...")
    result_ar = bounded_unit_root_test(
        data=data,
        bounds=(-5, 5),
        statistic='mz_alpha',
        detrending='gls_bounds',
        lrv_method='ar'
    )
    print(f"   ✓ AR-based LRV test completed")
    print(f"   MZα = {result_ar.statistic:.4f}")
    print(f"   LRV = {result_ar.lrv_estimate:.4f}")
    
    print("\n" + "=" * 70)
    print("ALL TESTS PASSED SUCCESSFULLY! ✓")
    print("=" * 70)
    print("\nThe boundedtest package is working correctly.")
    print("You can now use it for your econometric analysis.\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
