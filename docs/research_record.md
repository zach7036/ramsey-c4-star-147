# Research record

## Research question

Determine the exact value of `R(C4,K1,147)`.

Equivalent graph questions:

1. Does there exist a `C4`-free graph on 159 vertices with minimum degree at least 12?
2. Can a `C4`-free graph on 160 vertices have minimum degree at least 13?

A yes answer to the first and a no answer to the second prove the exact value 160.

## Lower-bound discovery

The ambient graph was the orthogonal-polarity graph `ER(13)` on the 183 points of `PG(2,13)`. Points were represented canonically as

- `(1,a,b)` for `a,b in F_13`,
- `(0,1,b)` for `b in F_13`,
- `(0,0,1)`.

Distinct points were joined when their dot product was zero modulo 13. A swap-based search selected 24 points to delete while preserving retained degree at least 12. The primary seed-555 search found a valid deletion after 1,207,474 iterations. The search was used only for discovery; the witness is reconstructed and audited exhaustively without trusting the heuristic.

## Upper-bound discovery

Local counting forced any hypothetical 160-vertex avoiding graph to be 13-regular. Every neighborhood was then forced to be `6K2 union K1`. This made the no-common-neighbor graph cubic and yielded

`A^2 = 12I + J - D`.

The common edges of `A` and `D` form a perfect matching, leaving a 2-factor. Exact moments through degree five, with one bounded trace parameter, allowed a rational quintic minorant and majorant for the positive spectral indicator. The resulting positive inertia was forced simultaneously above 78 and below 79.

## Falsification and validation

- Two separately discovered deletion sets were reconstructed from finite-field coordinates.
- Raw edge lists were checked independently without using the geometry.
- Every pair of retained vertices was checked to have at most one common neighbor.
- Exact degree, edge, and complement-degree statistics were checked.
- Deliberate edge-list corruptions were detected.
- The quintic factorization and rational moment sums were checked using a dependency-free standard-library script.
- A separate SymPy implementation recomputed the factorization and endpoint inequalities.
- The archived heuristic search command reproduced the primary deletion list exactly in the current environment.

## Final result

`R(C4,K1,147)=160`.

The result is exact; there are no sampling errors or confidence intervals. The remaining uncertainty is bibliographic and social rather than mathematical: the proof has not yet undergone external peer review, and no online search can prove universal novelty.
