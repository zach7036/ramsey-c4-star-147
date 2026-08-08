#!/usr/bin/env python3
"""Deterministically generate the two explicit lower-bound certificates."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from ramsey147_common import (
    Q,
    STAR_LEAVES,
    graph_stats,
    induced_witness,
    package_root,
)


def generate(label: str, deletion_file: Path) -> None:
    root = package_root()
    deleted = json.loads(deletion_file.read_text(encoding="utf-8"))
    if len(deleted) != 24 or len(set(deleted)) != 24:
        raise ValueError(f"{deletion_file.name}: expected 24 distinct indices")

    ambient_points, retained_ambient, retained_points, edges, adjacency = induced_witness(deleted)
    stats = graph_stats(adjacency)

    payload = {
        "description": (
            "Induced subgraph of the orthogonal-polarity graph ER(13), used as "
            "a lower-bound certificate for R(C4,K1,147)."
        ),
        "label": label,
        "field_order": Q,
        "ambient_order": len(ambient_points),
        "ambient_point_ordering": [
            "(1,a,b) for a=0..12, b=0..12 in lexicographic order",
            "(0,1,b) for b=0..12",
            "(0,0,1)",
        ],
        "adjacency_rule": "distinct x,y are adjacent iff x dot y == 0 (mod 13)",
        "deleted_ambient_indices": deleted,
        "deleted_points": [list(ambient_points[i]) for i in deleted],
        "retained_ambient_indices": retained_ambient,
        "retained_points": [list(point) for point in retained_points],
        "local_to_ambient": retained_ambient,
        "edges_local_labels": [list(edge) for edge in edges],
        "statistics": {
            "order": stats.order,
            "size": stats.size,
            "minimum_degree": stats.minimum_degree,
            "maximum_degree": stats.maximum_degree,
            "degree_distribution": {
                str(k): v for k, v in stats.degree_distribution.items()
            },
            "maximum_common_neighbors_between_distinct_vertices": (
                stats.maximum_common_neighbors
            ),
            "complement_maximum_degree": stats.complement_maximum_degree,
            "complement_avoids_star": f"K1,{STAR_LEAVES}",
        },
    }

    json_path = root / "data" / f"witness_147_{label}.json"
    edge_path = root / "data" / f"witness_147_{label}.edgelist"
    map_path = root / "data" / f"witness_147_{label}_vertex_map.csv"

    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    edge_path.write_text(
        "".join(f"{u} {v}\n" for u, v in edges), encoding="utf-8"
    )
    with map_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_vertex", "ambient_index", "x0", "x1", "x2", "degree"])
        for local_vertex, (ambient_index, point, neighbors) in enumerate(
            zip(retained_ambient, retained_points, adjacency)
        ):
            writer.writerow([local_vertex, ambient_index, *point, len(neighbors)])

    print(
        f"generated {label}: order={stats.order}, size={stats.size}, "
        f"degrees={stats.degree_distribution}, max_common={stats.maximum_common_neighbors}, "
        f"complement_Delta={stats.complement_maximum_degree}"
    )


def main() -> None:
    root = package_root()
    generate("primary", root / "data" / "deleted_points_primary_indices.json")
    generate("secondary", root / "data" / "deleted_points_secondary_indices.json")


if __name__ == "__main__":
    main()
