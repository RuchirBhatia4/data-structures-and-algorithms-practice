<!-- meta:start -->
# 133. Clone Graph

**LeetCode:** [133. Clone Graph](https://leetcode.com/problems/clone-graph/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given one node of a connected undirected graph, return a deep copy of the whole graph. Each node has a value and a list of neighbours; the copy must consist of new nodes connected the same way.

## Input

- `node`: a node of the graph (or `None`); each node has `val` and `neighbors`

## Output

- The copy of the given node, from which the whole copied graph is reachable.

## Constraints

- 0 to 100 nodes
- 1 ≤ `Node.val` ≤ 100, and values are unique
- No repeated edges or self-loops
- The graph is connected

## Edge cases

- Empty graph (`None`)
- Single node with no neighbours
- Cycles (do not copy a node twice)

## Examples

| Input | Output | Why |
|---|---|---|
| adjacency `[[2, 3], [1], [1]]` (node 1 linked to 2 and 3) | a new graph with the same adjacency | structure preserved |
| adjacency `[[]]` | one new node with no neighbours | single node |
| empty graph | `None` | nothing to copy |

> LeetCode describes a graph by an adjacency list where entry `i` lists the neighbours of the node with value `i + 1`.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Graphs · Hash Table · Depth-First Search · Breadth-First Search · Graph Theory
</details>
<!-- topics:end -->
