# Certificate data

The two canonical lower-bound proof inputs are the 24-point deletion lists:

- `deleted_points_primary_indices.json`
- `deleted_points_secondary_indices.json`

They refer to the deterministic ordering of the 183 projective points of `PG(2,13)` documented in `code/ramsey147_common.py`.

Run

```bash
python code/generate_witnesses.py
```

with `PYTHONPATH=code`, or simply run

```bash
bash run_all_checks.sh
```

to reconstruct the complete generated certificate files for both witnesses:

- `witness_147_primary.json`
- `witness_147_primary.edgelist`
- `witness_147_primary_vertex_map.csv`
- `witness_147_secondary.json`
- `witness_147_secondary.edgelist`
- `witness_147_secondary_vertex_map.csv`

The generator derives every edge directly from the finite-field dot-product rule. The independent edge-list checker then audits the generated labeled graph without using the finite-geometry construction.

The proof therefore depends only on the short deletion lists, the deterministic projective-point convention, and the checked source code—not on an opaque precomputed graph file.
