#!/usr/bin/env python3
"""Independent SymPy cross-check of the exact quintic inertia certificate.

This is deliberately separate from verify_spectral_certificate.py.  It asks
SymPy to expand/factor the polynomials and recompute the moment sums directly.
The standard-library verifier remains the dependency-free proof checker.
"""
from __future__ import annotations

import sympy as sp


def main() -> None:
    x, T = sp.symbols("x T", real=True)
    delta = sp.Integer(10554953355798500)
    q1 = sp.Integer(32954532192) * x**2 - sp.Integer(345828983244) * x + sp.Integer(1070139507025)
    q2 = sp.Integer(55381922156) * x**2 + sp.Integer(571556325813) * x + sp.Integer(1747833458735)
    q = sp.cancel((x + 3) * (11*x + 40)**2 * q1 / delta)
    expected_one_minus = -((3*x - 10)**2 * (8*x - 31) * q2) / delta
    assert sp.expand(1 - q - expected_one_minus) == 0

    assert sp.discriminant(q1, x) == -21466101685166657831664
    assert sp.discriminant(q2, x) == -60516872636399822819671
    assert sp.LC(sp.Poly(q1, x)) > 0 and sp.LC(sp.Poly(q2, x)) > 0
    assert 64 * 15 < 31**2

    moments = [159, -13, 1911, -277, 23439, T - 4893]
    poly = sp.Poly(sp.together(q).as_numer_denom()[0], x)
    coeffs = [sp.Rational(poly.nth(i), delta) for i in range(6)]
    lower_sum = sp.factor(sum(coeffs[i] * moments[i] for i in range(6)))
    expected_lower = sp.Rational(4, 2638738338949625) * (
        sp.Integer(249218649702) * T + sp.Integer(51609954472179121)
    )
    assert sp.simplify(lower_sum - expected_lower) == 0

    Q = sp.expand(1 - q.subs(x, -x))
    Qpoly = sp.Poly(sp.together(Q).as_numer_denom()[0], x)
    Qden = sp.together(Q).as_numer_denom()[1]
    upper_sum = sp.factor(sum(sp.Rational(Qpoly.nth(i), Qden) * moments[i] for i in range(6)))
    expected_upper = (
        sp.Integer(1993749197616) * T + sp.Integer(413822383511793005)
    ) / sp.Integer(5277476677899250)
    assert sp.simplify(upper_sum - expected_upper) == 0

    lower_at_zero = sp.simplify(lower_sum.subs(T, 0))
    upper_at_320 = sp.simplify(upper_sum.subs(T, 320))
    assert lower_at_zero > 78
    assert upper_at_320 < 79

    print("PASS: SymPy independently confirms both quintic factorizations")
    print(f"PASS: lower endpoint = {lower_at_zero} = {sp.N(lower_at_zero, 16)} > 78")
    print(f"PASS: upper endpoint = {upper_at_320} = {sp.N(upper_at_320, 16)} < 79")


if __name__ == "__main__":
    main()
