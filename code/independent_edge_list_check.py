#!/usr/bin/env python3
"""Coordinate-free audit of the raw edge-list certificates.

This deliberately does not import or use the finite-geometry construction.  It
checks only the labeled simple graph represented by each edge list.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path

ORDER = 159
EXPECTED_SIZE = 993
EXPECTED_DEGREES = {12: 81, 13: 78}
STAR_LEAVES = 147


def read_edges(path: Path) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) != 2:
            raise ValueError(f"{path}:{line_number}: expected two integers")
        edges.append((int(fields[0]), int(fields[1])))
    return edges


def audit(path: Path) -> None:
    edges = read_edges(path)
    if len(edges) != EXPECTED_SIZE:
        raise AssertionError(f"{path.name}: expected {EXPECTED_SIZE} edges, found {len(edges)}")

    adjacency = [set() for _ in range(ORDER)]
    normalized: set[tuple[int, int]] = set()
    for u, v in edges:
        if not (0 <= u < ORDER and 0 <= v < ORDER):
            raise AssertionError(f"endpoint outside 0..{ORDER - 1}: {(u, v)}")
        if u == v:
            raise AssertionError(f"loop: {(u, v)}")
        edge = (u, v) if u < v else (v, u)
        if edge in normalized:
            raise AssertionError(f"duplicate edge: {edge}")
        normalized.add(edge)
        adjacency[edge[0]].add(edge[1])
        adjacency[edge[1]].add(edge[0])

    degrees = [len(neighbors) for neighbors in adjacency]
    degree_distribution = dict(sorted(Counter(degrees).items()))
    if degree_distribution != EXPECTED_DEGREES:
        raise AssertionError(f"unexpected degree distribution: {degree_distribution}")

    max_common = 0
    common_histogram = Counter()
    for u, v in combinations(range(ORDER), 2):
        common = len(adjacency[u] & adjacency[v])
        common_histogram[common] += 1
        max_common = max(max_common, common)
    if max_common > 1:
        raise AssertionError("edge list contains a C4")

    complement_maximum_degree = max(ORDER - 1 - degree for degree in degrees)
    if complement_maximum_degree >= STAR_LEAVES:
        raise AssertionError("complement contains a K1,147")

    print(
        f"PASS {path.name}: n={ORDER}, m={len(edges)}, degrees={degree_distribution}, "
        f"max_common={max_common}, complement_Delta={complement_maximum_degree}, "
        f"common_hist={dict(sorted(common_histogram.items()))}"
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    audit(root / "data" / "witness_147_primary.edgelist")
    audit(root / "data" / "witness_147_secondary.edgelist")
    print("PASS: independent edge-list-only validation proves f(147) >= 160")


if __name__ == "__main__":
    main()
