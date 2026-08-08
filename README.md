# Exact determination of `R(C4, K1,147) = 160`

[![Verify research certificates](https://github.com/zach7036/ramsey-c4-star-147/actions/workflows/verify.yml/badge.svg)](https://github.com/zach7036/ramsey-c4-star-147/actions/workflows/verify.yml)

**Author:** Zach Waddle  
**Research draft:** August 7, 2026  
**Status:** complete AI-assisted research draft; not peer reviewed; external mathematical and bibliographic review requested

This repository contains the manuscript, explicit graph certificates, source code, archived verification logs, and complete reproducibility materials for the exact result

\[
\boxed{R(C_4,K_{1,147})=160}.
\]

The source-located pre-study interval was `159 <= R(C4,K1,147) <= 161`. The work closes that interval by supplying both an explicit lower-bound construction and an exact upper-bound contradiction.

> **Research-status note.** The certificates and exact arithmetic pass the included independent checks, but this result has not been peer reviewed. The novelty search found no prior exact report in the sources searched through August 7, 2026; that is evidence of novelty, not a logical guarantee that no unpublished or unindexed prior result exists.

## Read the paper

- **[Full manuscript (PDF)](paper/main.pdf)**
- **[LaTeX source](paper/main.tex)**
- **[Research record](docs/research_record.md)**
- **[Novelty-search log](docs/novelty_search_log.md)**
- **[Candidate screening and breakthrough criterion](docs/candidate_screening.md)**

## Main result

Let `f(n) = R(C4,K1,n)`.

### Lower bound: `f(147) >= 160`

Two independently stored induced subgraphs of the orthogonal-polarity graph `ER(13)` have:

- 159 vertices;
- 993 edges;
- degree distribution `12^81 13^78`;
- minimum degree 12;
- maximum common-neighbor multiplicity 1, hence no `C4`;
- complement maximum degree 146, hence no `K1,147` in the complement.

Therefore a 159-vertex coloring avoids both forbidden graphs and

`R(C4,K1,147) >= 160`.

The primary zero-based deletion certificate is

```text
[7, 8, 11, 39, 46, 47, 50, 52, 59, 60, 63, 84, 98, 99,
 101, 102, 117, 131, 133, 139, 143, 160, 169, 182]
```

The complete primary and secondary certificates are in [`data/`](data/).

### Upper bound: `f(147) <= 160`

Assume a `C4`-free graph `G` on 160 vertices has minimum degree at least 13. Exact local counting forces:

1. `G` is 13-regular;
2. every neighborhood has type `6K2 ∪ K1`;
3. the graph `D` joining pairs with no common `G`-neighbor is cubic;
4. with adjacency matrices `A,D`,

   `A^2 = 12I + J - D`;

5. every nonprincipal eigenvalue of `A` lies in

   `[-sqrt(15), -3] ∪ [3, sqrt(15)]`;

6. the first five nonprincipal moments are fixed up to `T = tr(AD^2)` with `0 <= T <= 320`.

An exact rational quintic inertia certificate then forces the number `N_+` of positive nonprincipal eigenvalues to satisfy

`78 < N_+ < 79`,

which is impossible because `N_+` is an integer. Thus no such 160-vertex graph exists and

`R(C4,K1,147) <= 160`.

Combining the two bounds gives the exact value.

## Verify the result

The core proof audit uses only the Python standard library:

```bash
bash run_all_checks.sh
```

Expected final line:

```text
ALL CORE CHECKS PASSED
```

The audit includes:

1. deterministic reconstruction of both finite-geometry witnesses;
2. a separate raw-edge-list-only validation;
3. deliberate corruption tests that must fail;
4. exact dependency-free verification of the spectral certificate;
5. an independent SymPy factorization cross-check when SymPy is available.

GitHub Actions runs the same core audit automatically on pushes and pull requests.

## Replay the discovery search

The witness-search heuristic is not part of the proof, but its stored discovery run can be reproduced:

```bash
bash replay_search.sh
```

Expected final line:

```text
PASS: seed-555 discovery replay exactly reproduced the primary deletion list
```

This requires a C++17 compiler.

## Repository structure

```text
paper/
  main.pdf                         complete manuscript
  main.tex                         LaTeX source
code/
  generate_witnesses.py            reconstruct certificates from finite geometry
  verify_witnesses.py              exact witness audit
  independent_edge_list_check.py   coordinate-free graph audit
  adversarial_mutation_tests.py    negative controls
  verify_spectral_certificate.py   exact upper-bound certificate check
  verify_spectral_certificate_sympy.py
  search_polarity_deletion.cpp     discovery heuristic
data/
  witness_147_primary.*            primary explicit certificate
  witness_147_secondary.*          independent secondary certificate
  deleted_points_*                 deletion lists
docs/
  candidate_screening.md
  novelty_search_log.md
  research_record.md
logs/
  verification.log
  search_primary.log
  search_secondary.log
  search_replay.log
manifest.json                      machine-readable result metadata
SHA256SUMS                         package integrity hashes
run_all_checks.sh                  one-command proof audit
replay_search.sh                   deterministic search replay
CITATION.cff                       citation metadata
```

## Reproducibility environment

The archived validation environment used:

- Python 3.13.5;
- SymPy 1.14.0 for the optional symbolic cross-check;
- g++ 14.2.0 for discovery replay;
- pdfTeX 1.40.26 for manuscript compilation.

The central proof checks themselves require only Python's standard library.

## What this changes

**Previously:** the source-located interval was `159–161`.

**Now:** the explicit 159-vertex construction raises the lower bound to 160, while the cubic-leave spectral certificate lowers the upper bound to 160.

**Result:** the interval is closed exactly at `160`.

Within this narrowly defined Ramsey-number program, exact resolution of a previously undetermined value was the pre-specified threshold for a candidate minor breakthrough. The result meets that threshold, subject to external expert review and independent bibliographic confirmation.

## Citation

Citation metadata are provided in [`CITATION.cff`](CITATION.cff). Until a peer-reviewed or archival publication exists, please cite this repository and identify the work as a research draft.
