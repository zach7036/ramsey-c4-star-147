# Literature and post-discovery novelty search log

Search date: 2026-08-07

## Sources checked

1. Radziszowski, *Small Ramsey Numbers*, Dynamic Survey 1, revision 18 (2026-04-24).
2. Chen, Zhang, and Zhang, *Star-quadrilateral Ramsey Number and Beyond* (2025), a recent dedicated survey.
3. Zhang, Chen, and Cheng, *Some Values of Ramsey Numbers for C4 versus Stars* (2017).
4. Zhang, Chen, and Cheng, *Polarity Graphs and Ramsey Numbers for C4 versus Stars* (2017).
5. Boza, *Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph*, arXiv:2409.12770v2 (2026-06-12).
6. Exact-phrase and formula searches across the general web, arXiv, Semantic Scholar-oriented results, DOI metadata, and GitHub.

## Adversarial exact queries

Representative exact searches included:

- `"R(C_4,K_{1,147})"`
- `"R(C4,K1,147)"`
- `"R(C_4,K_{1,147})=160"`
- `"f(147)" Ramsey C4 star`
- `quadrilateral star Ramsey 147 160`
- `"159-vertex" "C4-free" "minimum degree 12"`
- `"m^2+3" C4 star Ramsey`
- `"R(C4,K1,m^2+3)"`

The searches were repeated with spacing variants, Unicode/subscript variants, `quadrilateral` in place of `C4`, `star` in place of `K1,n`, and the equivalent wheel terminology used for `n>=6`.

## Source-located pre-study frontier

Let `f(n)=R(C4,K1,n)`.

- Zhang--Chen--Cheng prove, for odd prime-power `q>=5`, that
  `f(q(q-1)-t)=q^2-t` for even `t=2,4,...,2 ceil(q/4)`.
- With `q=13` and `t=8`, this gives `f(148)=161`.
- Chen's adjacent inequality `f(n-1)>=f(n)-2` gives `f(147)>=159`.
- Parsons' general upper estimate gives `f(147)<=161`.
- Boza's current theorem gives `f(m^2+3)<=m^2+m+4` only for `m congruent to 2 mod 6`; it does not cover `m=12`, where `m^2+3=147`.

Thus the source-located interval was `[159,161]`, and the exact value at 147 was not supplied by the known finite-field family or the current `m^2+3` theorem.

## Post-discovery conclusion

No prior exact report of `R(C4,K1,147)=160`, no matching 159-vertex minimum-degree-12 certificate, and no equivalent cubic-leave inertia proof was located in the sources and searches above.

This is evidence of novelty, not a logical proof that no unpublished manuscript, thesis, private computation, non-indexed proceedings paper, or newly posted work exists. The manuscript therefore uses the cautious language **"no prior report was located"** and requests specialist bibliographic review before formal publication.
