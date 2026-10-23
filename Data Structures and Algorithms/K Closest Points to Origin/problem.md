<!-- meta:start -->
# 973. K Closest Points to Origin

**LeetCode:** [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given points on a plane, return the `k` points closest to the origin `(0, 0)` by Euclidean distance. The answer is unique apart from ordering, and any order is accepted.

## Input

- `points`: list of `[x, y]` integer pairs
- `k`: number of points to return

## Output

- A list of the `k` closest points.

## Constraints

- 1 ≤ `k` ≤ `len(points)` ≤ 10⁴
- −10⁴ ≤ x, y ≤ 10⁴

## Edge cases

- `k` equal to the number of points
- Negative coordinates
- A point at the origin

## Examples

| Input | Output | Why |
|---|---|---|
| `points = [[2, 2], [1, -1], [-3, 0]], k = 1` | `[[1, -1]]` | squared distances are 8, 2 and 9 |
| `points = [[2, 2], [1, -1], [-3, 0]], k = 2` | `[[1, -1], [2, 2]]` | the two smallest distances |
| `points = [[0, 5]], k = 1` | `[[0, 5]]` | only one point |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Heap / Priority Queue · Array · Math · Divide and Conquer · Geometry · Sorting · Heap (Priority Queue) · Quickselect · K-D Tree
</details>
<!-- topics:end -->
