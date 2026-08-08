#!/usr/bin/env python3
"""Shared exact construction utilities for the f(147) certificate package.

All arithmetic is over the prime field F_13.  Projective points are normalized
so that the first nonzero coordinate is 1, in this deterministic order:

    (1,a,b), a=0..12, b=0..12;
    (0,1,b), b=0..12;
    (0,0,1).

Two distinct points are adjacent in the orthogonal-polarity graph when their
dot product is 0 modulo 13.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable, Sequence

Q = 13
AMBIENT_ORDER = Q * Q + Q + 1
TARGET_ORDER = 159
TARGET_MIN_DEGREE = 12
STAR_LEAVES = 147

Point = tuple[int, int, int]
Edge = tuple[int, int]


@dataclass(frozen=True)
class GraphStats:
    order: int
    size: int
    minimum_degree: int
    maximum_degree: int
    degree_distribution: dict[int, int]
    maximum_common_neighbors: int
    complement_maximum_degree: int


def projective_points(q: int = Q) -> list[Point]:
    """Return the canonical representatives of PG(2,q) for prime q."""
    points: list[Point] = []
    points.extend((1, a, b) for a in range(q) for b in range(q))
    points.extend((0, 1, b) for b in range(q))
    points.append((0, 0, 1))
    expected = q * q + q + 1
    if len(points) != expected or len(set(points)) != expected:
        raise AssertionError("projective point enumeration failed")
    return points


def dot_mod(x: Point, y: Point, q: int = Q) -> int:
    return sum(a * b for a, b in zip(x, y)) % q


def ambient_edges(points: Sequence[Point], q: int = Q) -> list[Edge]:
    """Generate the simple orthogonal-polarity graph on the supplied points."""
    return [
        (i, j)
        for i, j in combinations(range(len(points)), 2)
        if dot_mod(points[i], points[j], q) == 0
    ]


def induced_witness(
    deleted_indices: Iterable[int], q: int = Q
) -> tuple[list[Point], list[int], list[Point], list[Edge], list[set[int]]]:
    """Construct the retained induced graph, locally relabeled 0..N-1."""
    points = projective_points(q)
    raw_deleted = [int(v) for v in deleted_indices]
    deleted = sorted(set(raw_deleted))
    if len(deleted) != len(raw_deleted):
        raise ValueError("deleted point list contains duplicates")
    if len(deleted) != 24:
        raise ValueError(f"expected 24 distinct deleted points, found {len(deleted)}")
    if deleted and (deleted[0] < 0 or deleted[-1] >= len(points)):
        raise ValueError("deleted point index outside ambient graph")

    retained_ambient = [i for i in range(len(points)) if i not in set(deleted)]
    if len(retained_ambient) != TARGET_ORDER:
        raise AssertionError("retained order is not 159")
    local = {ambient: i for i, ambient in enumerate(retained_ambient)}

    edges: list[Edge] = []
    adjacency = [set() for _ in retained_ambient]
    for u, v in ambient_edges(points, q):
        if u in local and v in local:
            a, b = local[u], local[v]
            edges.append((a, b))
            adjacency[a].add(b)
            adjacency[b].add(a)

    retained_points = [points[i] for i in retained_ambient]
    return points, retained_ambient, retained_points, edges, adjacency


def adjacency_from_edges(order: int, edges: Iterable[Edge]) -> list[set[int]]:
    adjacency = [set() for _ in range(order)]
    seen: set[Edge] = set()
    for raw_u, raw_v in edges:
        u, v = int(raw_u), int(raw_v)
        if not 0 <= u < order or not 0 <= v < order:
            raise ValueError(f"edge {(u, v)} has endpoint outside 0..{order - 1}")
        if u == v:
            raise ValueError(f"loop at vertex {u}")
        if u > v:
            u, v = v, u
        if (u, v) in seen:
            raise ValueError(f"duplicate edge {(u, v)}")
        seen.add((u, v))
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency


def graph_stats(adjacency: Sequence[set[int]]) -> GraphStats:
    order = len(adjacency)
    degrees = [len(neighbors) for neighbors in adjacency]
    size = sum(degrees) // 2
    maximum_common_neighbors = 0
    for u, v in combinations(range(order), 2):
        common = len(adjacency[u].intersection(adjacency[v]))
        maximum_common_neighbors = max(maximum_common_neighbors, common)
    return GraphStats(
        order=order,
        size=size,
        minimum_degree=min(degrees),
        maximum_degree=max(degrees),
        degree_distribution=dict(sorted(Counter(degrees).items())),
        maximum_common_neighbors=maximum_common_neighbors,
        complement_maximum_degree=max(order - 1 - d for d in degrees),
    )


def has_c4(adjacency: Sequence[set[int]]) -> bool:
    """A simple graph has a C4 iff some pair has at least two common neighbors."""
    for u, v in combinations(range(len(adjacency)), 2):
        if len(adjacency[u].intersection(adjacency[v])) >= 2:
            return True
    return False


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]
