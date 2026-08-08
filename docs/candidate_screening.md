# Candidate screening record

Date fixed: 2026-08-07

## Breakthrough threshold fixed before the final target

The study distinguished four outcome levels before selecting a target:

- **Novel result:** not previously reported, but possibly narrow or expected.
- **Incremental advance:** a one-sided bound improvement, a larger search, or an additional witness that leaves the central uncertainty intact.
- **Minor breakthrough (minimum acceptable):** exact resolution of a source-located open cycle--star Ramsey number, or closure of a substantial published interval, with an independently auditable certificate and a proof that changes the accepted frontier.
- **Major breakthrough:** a general theorem resolving an infinite family or materially changing the broader theory.

The threshold was not lowered after computation. A new lower bound by itself, an unresolved solver run, or an unverified numerical pattern would not qualify.

## Ranking framework

Candidates were scored qualitatively on: importance, clarity of frontier, size of possible advance, tractability, available structure, independent verifiability, novelty risk, computation required, and impact. The optimization target was

`breakthrough potential x tractability x verifiability x novelty`.

| Rank | Candidate | Decisive bottleneck | Tractability assessment | Outcome |
|---:|---|---|---|---|
| 1 | `f(147)=R(C4,K1,147)` | Construct a 159-vertex `C4`-free graph of minimum degree 12 and exclude a 160-vertex graph of minimum degree 13 | Strong: `ER(13)` supplied a finite-geometry search space; the upper equality case forced a cubic leave amenable to exact spectral analysis | **Selected and solved: `f(147)=160`** |
| 2 | `f(146)` | Find a 158-vertex `C4`-free graph of minimum degree 12; parity would then make the matching upper bound unusually clean | Medium: `ER(13)` deletion searches repeatedly approached but did not reach the target | Rejected after no certified lower witness was found |
| 3 | `f(100)` | Find a 110-vertex `C4`-free graph of minimum degree 10; the upper side is parity-favorable | Medium: `ER(11)` candidates ended with two deficient vertices and no safe repair edge | Rejected after the lower certificate failed |
| 4 | `f(42)` | Decide a narrow two-value gap by exhaustive SAT after neighborhood symmetry reduction | Medium-low: exact encodings were feasible but the resulting instances did not finish with a checkable certificate during this study | Deferred; unresolved computations were not treated as results |
| 5 | `f(52)` | Decide existence of an 8-regular `C4`-free graph on 60 vertices | Low-medium: the structural reduction was clean, but the remaining regular-graph search was too broad for a defensible completion | Deferred |

The selected target was not simply the first one attempted. It was the first candidate for which both sides of an exact determination became independently certifiable.

## Why the selected result crosses the fixed threshold

Before the study, source-located results implied `159 <= f(147) <= 161`. The new work gives an explicit lower certificate at 159 vertices and an analytic nonexistence proof at 160 vertices, establishing the exact value. This eliminates the full uncertainty, extends the published `q=13` exact sequence one step beyond its even-parameter range, and introduces a cubic-leave spectral certificate for the residue class where the earlier triangle-divisibility argument does not close. It is therefore classified as a **candidate minor breakthrough in this narrowly defined Ramsey-number line**, subject to external review.
