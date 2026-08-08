#!/usr/bin/env python3
"""Negative controls for the lower-bound graph certificate.

The tests deliberately corrupt the primary witness in several different ways
and confirm that the exact validation invariants reject the corruptions.
"""
from __future__ import annotations

from itertools import combinations
from pathlib import Path

from ramsey147_common import adjacency_from_edges, graph_stats, has_c4

ORDER = 159
EXPECTED_SIZE = 993


def read_edges(path: Path) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split())) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    edges = read_edges(root / "data" / "witness_147_primary.edgelist")
    base = adjacency_from_edges(ORDER, edges)
    assert not has_c4(base) and graph_stats(base).minimum_degree == 12

    # Negative control 1: remove an edge.  The certificate then has the wrong
    # size and no longer has the archived degree distribution.
    removed = adjacency_from_edges(ORDER, edges[1:])
    removed_stats = graph_stats(removed)
    assert removed_stats.size == EXPECTED_SIZE - 1
    assert removed_stats.degree_distribution != {12: 81, 13: 78}

    # Negative control 2: duplicate an edge.  The graph parser must reject it.
    try:
        adjacency_from_edges(ORDER, edges + [edges[0]])
    except ValueError as exc:
        assert "duplicate edge" in str(exc)
    else:
        raise AssertionError("duplicate-edge corruption was not detected")

    # Negative control 3: add a nonedge that closes a 4-cycle.  Find such an
    # edge algorithmically rather than hard-coding it.
    edge_set = set(edges)
    corrupting_edge = None
    for u, v in combinations(range(ORDER), 2):
        if (u, v) in edge_set:
            continue
        test = [neighbors.copy() for neighbors in base]
        test[u].add(v)
        test[v].add(u)
        if has_c4(test):
            corrupting_edge = (u, v)
            break
    assert corrupting_edge is not None
    corrupted = adjacency_from_edges(ORDER, edges + [corrupting_edge])
    assert has_c4(corrupted)

    print("PASS: removed-edge corruption changes the exact degree certificate")
    print("PASS: duplicate-edge corruption is rejected by the parser")
    print(f"PASS: added edge {corrupting_edge} is detected as creating a C4")


if __name__ == "__main__":
    main()
