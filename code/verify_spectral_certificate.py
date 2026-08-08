#!/usr/bin/env python3
"""Exact standard-library verification of the 160-vertex upper-bound certificate.

The script uses only integer and rational arithmetic.  It checks:
  * the forced regularity/local-counting parameters;
  * the five nonprincipal spectral moments;
  * both factorizations of the quintic separator;
  * positivity of the quadratic cofactors via exact discriminants;
  * the two strict inertia inequalities for every 0 <= T <= 320.

The graph-theoretic lemmas connecting these calculations are written out in the
paper; this script verifies every nontrivial numerical and polynomial identity.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


Poly = list[int]  # ascending powers


def trim(poly: Poly) -> Poly:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(a: Poly, b: Poly) -> Poly:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def scale(a: Poly, c: int) -> Poly:
    return trim([c * value for value in a])


def multiply(a: Poly, b: Poly) -> Poly:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def power(a: Poly, exponent: int) -> Poly:
    out = [1]
    for _ in range(exponent):
        out = multiply(out, a)
    return out


def rational_moment_sum(coefficients: Iterable[Fraction], moments: Iterable[Fraction]) -> Fraction:
    return sum((c * s for c, s in zip(coefficients, moments)), Fraction(0))


def main() -> None:
    # Ramsey and local-counting parameters.
    n_star = 147
    order = 160
    minimum_degree = order - n_star
    assert minimum_degree == 13

    # For every vertex v in a C4-free graph, 13*d(v) <= 159+d(v).
    # Together with d(v)>=13 this forces d(v)=13.
    assert 13 * 13 <= 159 + 13
    assert 13 * 14 > 159 + 14
    degree = 13

    outside_closed_neighborhood = order - 1 - degree
    assert outside_closed_neighborhood == 146

    # If t_v is the matching size inside N(v), then 156-2t_v <= 146,
    # while t_v<=floor(13/2)=6.  Hence t_v is 5 or 6.
    possible_t = [t for t in range(7) if degree * (degree - 1) - 2 * t <= 146]
    assert possible_t == [5, 6]

    # The t_v=5 partition has ten blocks of size 11 and three of size 12.
    assert 10 * 11 + 3 * 12 == 146
    # Its isolated-vertex degree bound is 1 + 11 = 12 < 13.
    assert 1 + 11 < degree

    triangles = order * 6 // 3
    assert triangles == 320

    # The leave degree is 159 - 13*12 = 3.
    leave_degree = order - 1 - degree * (degree - 1)
    assert leave_degree == 3

    # T=tr(A D^2)=tr(A C^2), with 0<=T<=2n.
    t_min, t_max = 0, 2 * order
    assert t_max == 320

    # Nonprincipal moment vector s_j=sum lambda_i^j for j=0,...,5.
    # s5 is affine in T.
    s0 = order - 1
    s1 = -degree
    s2 = order * degree - degree**2
    s3 = 6 * triangles - degree**3
    s4 = order * degree * (2 * degree - 1) - degree**4
    s5_constant = -4893
    assert (s0, s1, s2, s3, s4) == (159, -13, 1911, -277, 23439)

    # Verify the D^2 trace constant independently:
    # D^2=A^4-24A^2+144I-154J,
    # T=tr(A^5)-24tr(A^3)-154tr(AJ).
    trace_a3 = 6 * triangles
    trace_aj = degree * order
    trace_offset = 24 * trace_a3 + 154 * trace_aj
    assert trace_offset == 366400
    assert trace_offset - degree**5 == -4893

    # Exact quintic separator q(x)=q_num(x)/Delta.
    delta = 10554953355798500
    q1 = [1070139507025, -345828983244, 32954532192]
    q2 = [1747833458735, 571556325813, 55381922156]

    q_num = multiply(
        multiply([3, 1], power([40, 11], 2)),
        q1,
    )
    assert len(q_num) == 6

    # Delta-q_num = -(3x-10)^2(8x-31)Q2.
    one_minus_q_num = add([delta], scale(q_num, -1))
    factored_one_minus = scale(
        multiply(multiply(power([-10, 3], 2), [-31, 8]), q2),
        -1,
    )
    assert one_minus_q_num == factored_one_minus

    # Exact positivity of both quadratic cofactors.
    disc_q1 = q1[1] ** 2 - 4 * q1[2] * q1[0]
    disc_q2 = q2[1] ** 2 - 4 * q2[2] * q2[0]
    assert disc_q1 == -21466101685166657831664
    assert disc_q2 == -60516872636399822819671
    assert disc_q1 < 0 and q1[2] > 0
    assert disc_q2 < 0 and q2[2] > 0

    # Exact support endpoint comparison sqrt(15)<31/8.
    assert 64 * 15 < 31**2

    q_coefficients = [Fraction(value, delta) for value in q_num]
    moments_t0 = [
        Fraction(s0),
        Fraction(s1),
        Fraction(s2),
        Fraction(s3),
        Fraction(s4),
        Fraction(s5_constant),
    ]

    # q lower-bounds the positive inertia indicator sum.
    q_sum_t0 = rational_moment_sum(q_coefficients, moments_t0)
    q_slope = q_coefficients[5]
    assert q_slope > 0
    assert q_sum_t0 == Fraction(206439817888716484, 2638738338949625)
    assert q_sum_t0 - 78 == Fraction(618227450645734, 2638738338949625)
    assert q_sum_t0 > 78

    # Q(x)=1-q(-x) upper-bounds the same indicator.
    majorant_coefficients = [Fraction(1) - q_coefficients[0]] + [
        -((-1) ** i) * q_coefficients[i] for i in range(1, 6)
    ]
    # Equivalent: coefficient of x^i is -(-1)^i q_i, except the constant 1-q_0.
    majorant_sum_t0 = rational_moment_sum(majorant_coefficients, moments_t0)
    majorant_slope = majorant_coefficients[5]
    assert majorant_slope > 0
    majorant_sum_tmax = majorant_sum_t0 + majorant_slope * t_max
    assert majorant_sum_tmax == Fraction(3315683066040241, 42219813423194)
    assert 79 - majorant_sum_tmax == Fraction(19682194392085, 42219813423194)
    assert majorant_sum_tmax < 79

    # Cross-check the closed forms used in the manuscript.
    q_closed_t0 = Fraction(4 * 51609954472179121, 2638738338949625)
    q_closed_slope = Fraction(4 * 249218649702, 2638738338949625)
    assert q_sum_t0 == q_closed_t0
    assert q_slope == q_closed_slope

    majorant_closed_t0 = Fraction(413822383511793005, 5277476677899250)
    majorant_closed_slope = Fraction(1993749197616, 5277476677899250)
    assert majorant_sum_t0 == majorant_closed_t0
    assert majorant_slope == majorant_closed_slope

    # Since N_+ is an integer, N_+>78 and N_+<79 is impossible.
    print("PASS: local counting forces a 13-regular equality case with six triangles per vertex")
    print(f"PASS: leave graph degree={leave_degree}, spectral support is |lambda| in [3,sqrt(15)]")
    print(f"PASS: q-factor discriminants are {disc_q1} and {disc_q2}")
    print(f"PASS: lower inertia sum at T=0 is {q_sum_t0} = {float(q_sum_t0):.12f} > 78")
    print(
        "PASS: upper inertia sum at T=320 is "
        f"{majorant_sum_tmax} = {float(majorant_sum_tmax):.12f} < 79"
    )
    print("PASS: no 160-vertex C4-free graph has minimum degree 13; therefore f(147) <= 160")


if __name__ == "__main__":
    main()
