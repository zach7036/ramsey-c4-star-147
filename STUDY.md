# Exact determination of a cycle–star Ramsey number beyond the published q=13 range

## `R(C4,K1,147) = 160`

**Author:** Zach Waddle  
**Research draft:** August 7, 2026  
**Status:** AI-assisted research draft; not peer reviewed; external mathematical and bibliographic review requested.

## Abstract

Let `f(n)=R(C4,K1,n)`. The source-located literature left the value at `n=147` in the interval

`159 <= f(147) <= 161`.

This study closes that interval exactly. For the lower bound, two explicit induced subgraphs of the orthogonal-polarity graph `ER(13)` are constructed on 159 vertices. Each is `C4`-free, has 993 edges, degree distribution `12^81 13^78`, and minimum degree 12. Its complement therefore has maximum degree 146 and contains no `K1,147`, proving `f(147)>=160`.

For the upper bound, assume a `C4`-free graph `G` on 160 vertices has minimum degree at least 13. Local counting forces `G` to be 13-regular and every neighborhood to be `6K2 union K1`. The graph `D` joining pairs with no common `G`-neighbor is then cubic and satisfies

`A^2 = 12I + J - D`.

The common edges of `G` and `D` form a perfect matching, leaving a spanning 2-factor. This confines the nonprincipal spectrum of `A` to

`[-sqrt(15),-3] union [3,sqrt(15)]`

and determines the first five nonprincipal moments up to one trace parameter `T` with `0<=T<=320`. An exact rational quintic minorant and reflected majorant for the positive-eigenvalue indicator force the number of positive nonprincipal eigenvalues to satisfy

`78 < N_+ < 79`,

an integer impossibility. Hence `f(147)<=160`, and therefore

## Main theorem

$$
\boxed{R(C_4,K_{1,147})=160}.
$$

The result survived independent finite-geometry reconstruction, coordinate-free edge-list auditing, deliberate corruption tests, exact rational verification, a separate SymPy implementation, and deterministic replay of the witness search. No prior exact report of this value was located in the searches documented in `docs/novelty_search_log.md`. That is evidence of novelty, not a guarantee against unpublished or unindexed prior work.

---

## 1. Breakthrough criterion

The threshold was fixed before the final target was selected.

- **Novel result:** something not previously reported, regardless of importance.
- **Incremental advance:** a one-sided bound improvement, larger computation, or additional witness that leaves the central uncertainty unresolved.
- **Minor breakthrough:** exact resolution of a source-located open Ramsey number, closure of a substantial interval, or another result that decisively changes the frontier of the specific problem.
- **Major breakthrough:** a broader infinite-family or asymptotic advance.

For this project, the minimum acceptable outcome was the exact determination of an unresolved `C4`-versus-star Ramsey number with independently auditable lower- and upper-bound certificates. A new lower bound alone, an unfinished solver computation, or a heuristic numerical pattern would not qualify.

The candidate-screening record is preserved in `docs/candidate_screening.md`.

---

## 2. State of the frontier

For graphs `H1,H2`, `R(H1,H2)` is the least `N` such that every graph `G` on `N` vertices contains `H1` or its complement contains `H2`. Write

`f(n)=R(C4,K1,n)`.

The complement avoids `K1,n` exactly when its maximum degree is at most `n-1`. Thus `f(n)` is the smallest `N` for which no `C4`-free graph on `N` vertices can have minimum degree at least `N-n`.

Three established results locate the target:

1. Chen's adjacent-value inequality gives `f(n-1)>=f(n)-2`.
2. Parsons gives the standard general upper estimate for this family.
3. Zhang, Chen, and Cheng proved, for odd prime powers `q>=5`, an exact family

   `f(q(q-1)-t)=q^2-t`

   for even `t=2,4,...,2 ceil(q/4)`.

Taking `q=13,t=8` gives `f(148)=161`. Therefore Chen's inequality yields `f(147)>=159`, while Parsons gives `f(147)<=161`:

$$
159\le f(147)\le161.
$$

The current Boza theorem for parameters `m^2+3` applies to `m congruent 2 (mod 6)` and does not cover `m=12`, where `m^2+3=147`.

The exact research question was therefore: **is `f(147)` equal to 159, 160, or 161?**

---

## 3. Lower bound: an explicit 159-vertex construction

### 3.1 Ambient finite geometry

Work over the field `F_13`. Use the canonical representatives of the 183 projective points of `PG(2,13)`:

- `(1,a,b)` for `a,b in F_13`;
- `(0,1,b)` for `b in F_13`;
- `(0,0,1)`.

The orthogonal-polarity graph `ER(13)` joins two distinct points `x,y` exactly when

`x dot y = 0 (mod 13)`.

Any two distinct projective points have at most one common orthogonal projective point, because two independent linear equations in a three-dimensional vector space have a one-dimensional common solution space. Hence `ER(13)` is `C4`-free.

### 3.2 Primary deletion certificate

Delete the following 24 zero-based ambient point indices:

```text
[7,8,11,39,46,47,50,52,59,60,63,84,98,99,101,102,
 117,131,133,139,143,160,169,182]
```

The retained induced graph has exactly:

- order `159`;
- size `993`;
- degree distribution `12^81 13^78`;
- minimum degree `12`;
- maximum common-neighbor multiplicity `1`.

Therefore it is `C4`-free. Its complement has maximum degree

`158 - 12 = 146`,

so the complement contains no `K1,147`. Thus

$$
f(147)\ge160.
$$

### 3.3 Independent secondary certificate

A separate search seed produced a distinct 24-point deletion:

```text
[2,6,15,19,31,32,48,62,67,82,91,116,119,125,131,133,
 145,147,149,150,154,162,170,173]
```

It yields the same certified statistics: 159 vertices, 993 edges, degree distribution `12^81 13^78`, maximum common-neighbor multiplicity 1, and complement maximum degree 146.

The deletion lists are stored in `data/`. `code/generate_witnesses.py` deterministically reconstructs the complete JSON certificates, raw edge lists, and vertex maps from the finite-geometry rule.

---

## 4. Upper bound: no 160-vertex avoiding graph exists

Assume for contradiction that `G` is `C4`-free on 160 vertices and that its complement contains no `K1,147`. Then

`delta(G) >= 160-147 = 13`.

### 4.1 Forced 13-regularity

Fix a vertex `v` of degree `d`, and let `U=N(v)`. In a `C4`-free graph, `G[U]` has maximum degree at most one, and every vertex outside `N[v]` has at most one neighbor in `U`. Therefore

$$
\sum_{u\in U} d(u)\le159+d.
$$

Since every `u` has degree at least 13,

$$
13d\le159+d.
$$

Thus `d<=13.25`, and because `d>=13`, every vertex has degree exactly 13. Hence `G` is 13-regular.

### 4.2 Every neighborhood is `6K2 union K1`

For a vertex `v`, let `t_v` be the number of edges inside `N(v)`. Since `N(v)` induces a matching, `t_v<=6`.

The 13 neighbors of `v` send

`13*12 - 2t_v = 156 - 2t_v`

edges to the 146 vertices outside `N[v]`. Each outside vertex receives at most one such edge, so

`156-2t_v <= 146`,

which gives `t_v in {5,6}`.

Suppose `t_v=5`. Then `N(v)` consists of five matched pairs and three isolated vertices. For each `u in N(v)`, set

`A_u=N(u) \ N[v]`.

The `A_u` are pairwise disjoint. The ten matched neighborhood vertices have blocks of size 11, and the three isolated neighborhood vertices have blocks of size 12, so

`10*11 + 3*12 = 146`.

Hence the blocks partition the entire outside set. Choose one matched pair `u1u2`. The graph induced by `A_u1` has maximum degree one and odd order 11, so it contains an isolated vertex `w`. The vertex `w` has no neighbor in `A_u2`, since such an edge would create a `C4`; it has at most one neighbor in each of the remaining 11 blocks; and its only neighbor in `N(v)` is `u1`. Therefore

`d(w) <= 1+11 = 12`,

contradicting 13-regularity.

Thus

$$
t_v=6\quad\text{for every }v.
$$

Every neighborhood is therefore `6K2 union K1`, and the graph has

`160*6/3 = 320`

triangles.

### 4.3 The cubic leave

Define a graph `D` on the same vertices by joining two distinct vertices exactly when they have no common neighbor in `G`.

From any fixed vertex, the `13*12=156` nonbacktracking walks of length two have distinct endpoints because `G` is `C4`-free. There are 159 other vertices, so exactly three of them have no common neighbor with the fixed vertex. Thus `D` is cubic.

Let `A,D,J,I` denote the adjacency matrices of `G`, `D`, the all-one matrix, and the identity. Then entrywise common-neighbor counting gives

$$
A^2=12I+J-D.
$$

Because every neighborhood is `6K2 union K1`, each vertex has exactly one incident edge of `G` lying in no triangle. Those edges are precisely the common edges of `G` and `D`, and they form a perfect matching `M`. Therefore

`C=D-M`

is a spanning 2-regular graph.

### 4.4 Spectral support

On the orthogonal complement of the all-one vector, `J=0`, so

$$
D=12I-A^2.
$$

Every eigenvalue of the cubic graph `D` lies in `[-3,3]`. Hence every nonprincipal eigenvalue `lambda` of `A` satisfies

$$
9\le\lambda^2\le15,
$$

or

$$
\lambda\in[-\sqrt{15},-3]\cup[3,\sqrt{15}].
$$

This spectral gap around zero is the key structural feature.

### 4.5 Exact moments

Let `lambda_1,...,lambda_159` be the nonprincipal eigenvalues of `A`, and let

`s_j=sum_i lambda_i^j`.

Exact walk counting gives

```text
s0 = 159
s1 = -13
s2 = 1911
s3 = -277
s4 = 23439
s5 = T - 4893
```

where

`T = tr(A D^2)`.

Since `D=M+C`, `M` is a perfect matching, and `C` is 2-regular, the mixed trace terms vanish and

`T=tr(A C^2)`.

Each row of `C^2` has total off-diagonal weight 2, so

$$
0\le T\le2\cdot160=320.
$$

Thus the first five nonprincipal moments are known exactly, with only a bounded one-dimensional freedom remaining.

---

## 5. Exact quintic inertia certificate

Set

```text
Delta = 10554953355798500
```

and define

$$
q(x)=\frac{(x+3)(11x+40)^2Q_1(x)}{\Delta},
$$

where

$$
Q_1(x)=32954532192x^2-345828983244x+1070139507025.
$$

Its discriminant is

```text
-21466101685166657831664 < 0,
```

so `Q1(x)>0` for all real `x`.

An exact polynomial identity gives

$$
1-q(x)=
-\frac{(3x-10)^2(8x-31)Q_2(x)}{\Delta},
$$

where

$$
Q_2(x)=55381922156x^2+571556325813x+1747833458735.
$$

The discriminant of `Q2` is

```text
-60516872636399822819671 < 0,
```

so `Q2(x)>0` for all real `x`. Also `sqrt(15)<31/8`.

Therefore, on the negative spectral interval, `q(x)<=0`, while on the positive interval, `q(x)<=1`. Hence

$$
q(x)\le\mathbf 1_{x>0}
$$

throughout the entire allowed spectral support.

Define the reflected majorant

$$
Q(x)=1-q(-x).
$$

Then

$$
q(x)\le\mathbf 1_{x>0}\le Q(x).
$$

Let `N_+` be the number of positive nonprincipal eigenvalues. Substituting the exact moments gives

$$
\sum_i q(\lambda_i)
=
\frac{4(249218649702T+51609954472179121)}{2638738338949625}.
$$

The coefficient of `T` is positive, so its minimum occurs at `T=0`, where

$$
\sum_i q(\lambda_i)
=
\frac{206439817888716484}{2638738338949625}
\approx78.234289031815>78.
$$

Thus

$$
N_+>78.
$$

For the majorant,

$$
\sum_i Q(\lambda_i)
=
\frac{1993749197616T+413822383511793005}{5277476677899250}.
$$

Again the coefficient of `T` is positive, so its maximum occurs at `T=320`, where

$$
\sum_i Q(\lambda_i)
=
\frac{3315683066040241}{42219813423194}
\approx78.533816168376<79.
$$

Therefore

$$
N_+<79.
$$

Together,

$$
78<N_+<79,
$$

which is impossible because `N_+` is an integer.

Consequently no `C4`-free graph on 160 vertices can have minimum degree 13, so

$$
f(147)\le160.
$$

Combining this with the explicit 159-vertex construction proves the main theorem.

---

## 6. Validation and falsification attempts

The candidate result was treated as potentially wrong and attacked in several independent ways.

### Lower certificate

1. **Finite-geometry reconstruction.** The verifier reconstructs all 183 projective points and all polarity edges from the dot-product rule, applies each deletion list, and recomputes the graph from scratch.
2. **Coordinate-free audit.** A separate program ignores the projective coordinates and checks only the generated raw edge list.
3. **All-pairs `C4` test.** Every pair of retained vertices is checked for common-neighbor multiplicity; the maximum is exactly 1.
4. **Independent witness.** A second deletion list gives a distinct graph with the same extremal statistics.
5. **Negative controls.** Removing an edge changes the exact degree certificate; duplicating an edge is rejected; and adding a selected nonedge is detected as creating a `C4`.
6. **Discovery replay.** Seed 555 reproduces the primary deletion list after 1,207,474 iterations in the archived environment. The search is not trusted as proof; the output is reverified independently.

### Upper certificate

1. **Dependency-free arithmetic checker.** `code/verify_spectral_certificate.py` verifies every integer constant, polynomial identity, discriminant, moment substitution, and rational endpoint inequality using Python's standard library.
2. **Separate symbolic implementation.** `code/verify_spectral_certificate_sympy.py` independently expands and checks both quintic factorizations and moment sums with SymPy.
3. **Whole-interval check.** The lower bound is evaluated at the smallest possible `T`, and the upper bound at the largest possible `T`, so the contradiction holds for every `0<=T<=320`.
4. **Exact margins.** The inequalities are rational and strict; no floating-point decision is used.

Run the complete proof audit with

```bash
bash run_all_checks.sh
```

Expected final line:

```text
ALL CORE CHECKS PASSED
```

Replay the discovery search with

```bash
bash replay_search.sh
```

Expected final line:

```text
PASS: seed-555 discovery replay exactly reproduced the primary deletion list
```

---

## 7. Quantitative change to the frontier

| Quantity | Before this study | Result here |
|---|---:|---:|
| `R(C4,K1,147)` | `159–161` | **160** |
| 159-vertex lower certificate | not located | two explicit certificates |
| 160-vertex equality case | not excluded | excluded analytically |
| q=13 exact sequence | cited even offsets through `t=8` | additional exact odd step `t=9` |

This is narrow in scope but decisive: the entire three-value uncertainty is removed.

---

## 8. Novelty review after discovery

The post-discovery search checked the current Small Ramsey Numbers survey, the recent dedicated star-quadrilateral survey, the principal 2015–2017 construction papers, Boza's current arXiv revision, exact-form web searches, arXiv-oriented results, DOI metadata, and GitHub searches.

No prior report of

`R(C4,K1,147)=160`,

the displayed 159-vertex deletion certificates, or an equivalent cubic-leave quintic inertia proof was located as of August 7, 2026.

The detailed search record is in `docs/novelty_search_log.md`. This cannot exclude unpublished manuscripts, private computations, non-indexed theses, or newly posted work.

---

## 9. Why this qualifies as a candidate minor breakthrough

The pre-specified threshold was exact resolution of a genuinely unresolved cycle–star Ramsey number with independently auditable certificates. This study does that: it replaces the interval `159–161` with the exact value 160 and supplies both a constructive lower certificate and a complete analytic upper proof.

It is not claimed as a major field-wide breakthrough. It does not establish a new asymptotic bound, classify all extremal graphs, or prove an infinite family. The appropriate claim is **candidate minor breakthrough in this narrowly defined Ramsey-number program**, pending external expert verification and bibliographic review.

---

## 10. Limitations

- The manuscript has not been peer reviewed.
- Universal novelty cannot be proved by online search.
- The lower witness was discovered heuristically, although its validity is completely independent of the heuristic.
- No uniqueness or isomorphism classification of the 159-vertex witnesses is claimed.
- The spectral method is tailored to this cubic-leave equality case and is not itself an infinite-family theorem.
- No new asymptotic Ramsey bound is established.

There is no statistical sampling uncertainty in the theorem: the certificates and arithmetic are finite and exact.

---

## 11. References

1. T. D. Parsons, “Ramsey Graphs and Block Designs, I,” *Transactions of the American Mathematical Society* 209 (1975), 33–44.
2. T. D. Parsons, “Graphs from Projective Planes,” *Aequationes Mathematicae* 14 (1976), 167–189.
3. G. Chen, “A Result on C4-Star Ramsey Numbers,” *Discrete Mathematics* 163 (1997), 243–246.
4. Y. Wu, Y. Sun, R. Zhang, and S. P. Radziszowski, “Ramsey numbers of C4 versus wheels and stars,” *Graphs and Combinatorics* 31 (2015), 2437–2446.
5. X. Zhang, Y. Chen, and T. C. E. Cheng, “Some Values of Ramsey Numbers for C4 versus Stars,” *Finite Fields and Their Applications* 45 (2017), 73–85.
6. X. Zhang, Y. Chen, and T. C. E. Cheng, “Polarity Graphs and Ramsey Numbers for C4 versus Stars,” *Discrete Mathematics* 340 (2017), 655–660.
7. Y. Chen, X. Zhang, and Y. Zhang, “Star-quadrilateral Ramsey Number and Beyond,” *Advances in Mathematics (China)* 54(2) (2025), 292–314.
8. L. Boza, “Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph,” arXiv:2409.12770v2, revised June 12, 2026.
9. S. P. Radziszowski, “Small Ramsey Numbers,” *Electronic Journal of Combinatorics*, Dynamic Survey 1, revision 18, April 24, 2026.

---

## AI-assistance disclosure

This investigation was carried out through an AI-assisted research workflow coordinated for Zach Waddle. OpenAI GPT-5.6 Pro searched and synthesized the literature, generated and screened candidate targets, executed computational searches, derived and stress-tested the proof, created exact verification code, and drafted the research materials. The named author is responsible for deciding whether to circulate, revise, or submit the result. Independent human mathematical and bibliographic review is explicitly requested.
