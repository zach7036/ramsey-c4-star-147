#!/usr/bin/env python3
"""Exact finite-geometry reconstruction audit for both lower-bound witnesses."""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations

from ramsey147_common import (
    Q,
    STAR_LEAVES,
    TARGET_MIN_DEGREE,
    TARGET_ORDER,
    adjacency_from_edges,
    ambient_edges,
    dot_mod,
    graph_stats,
    has_c4,
    package_root,
    projective_points,
)


def verify(label: str) -> dict[str, object]:
    root = package_root()
    path = root / "data" / f"witness_147_{label}.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    assert data["field_order"] == Q
    points = projective_points(Q)
    assert len(points) == 183
    assert len(set(points)) == 183
    assert Counter(sum(x * x for x in p) % Q == 0 for p in points) == Counter(
        {False: 169, True: 14}
    )

    deleted = data["deleted_ambient_indices"]
    retained = data["retained_ambient_indices"]
    assert len(deleted) == len(set(deleted)) == 24
    assert len(retained) == len(set(retained)) == TARGET_ORDER
    assert set(deleted).isdisjoint(retained)
    assert set(deleted).union(retained) == set(range(183))
    assert [list(points[i]) for i in deleted] == data["deleted_points"]
    assert [list(points[i]) for i in retained] == data["retained_points"]
    assert retained == data["local_to_ambient"]

    local = {ambient: i for i, ambient in enumerate(retained)}
    expected_edges = []
    for u, v in ambient_edges(points, Q):
        if u in local and v in local:
            expected_edges.append((local[u], local[v]))
    stored_edges = [tuple(edge) for edge in data["edges_local_labels"]]
    assert stored_edges == expected_edges

    adjacency = adjacency_from_edges(TARGET_ORDER, stored_edges)
    stats = graph_stats(adjacency)
    assert stats.order == TARGET_ORDER
    assert stats.size == 993
    assert stats.minimum_degree == TARGET_MIN_DEGREE
    assert stats.maximum_degree == 13
    assert stats.degree_distribution == {12: 81, 13: 78}
    assert stats.maximum_common_neighbors == 1
    assert not has_c4(adjacency)
    assert stats.complement_maximum_degree == 146
    assert stats.complement_maximum_degree < STAR_LEAVES

    # Directly recheck every stored edge and every nonedge against the field rule.
    stored_edge_set = set(stored_edges)
    for u, v in combinations(range(TARGET_ORDER), 2):
        orthogonal = dot_mod(points[retained[u]], points[retained[v]], Q) == 0
        assert ((u, v) in stored_edge_set) == orthogonal

    # Explicit C4-equivalent audit: no pair has two common neighbors.
    common_neighbor_histogram = Counter()
    for u, v in combinations(range(TARGET_ORDER), 2):
        common_neighbor_histogram[len(adjacency[u] & adjacency[v])] += 1
    assert not any(count for common, count in common_neighbor_histogram.items() if common >= 2)

    return {
        "label": label,
        "order": stats.order,
        "size": stats.size,
        "degree_distribution": stats.degree_distribution,
        "maximum_common_neighbors": stats.maximum_common_neighbors,
        "complement_maximum_degree": stats.complement_maximum_degree,
        "common_neighbor_histogram": dict(sorted(common_neighbor_histogram.items())),
        "ramsey_consequence": "f(147) >= 160",
    }


def main() -> None:
    results = [verify("primary"), verify("secondary")]
    for result in results:
        print(json.dumps(result, sort_keys=True))
    print("PASS: both finite-geometry witnesses reconstruct exactly and prove f(147) >= 160")


if __name__ == "__main__":
    main()
