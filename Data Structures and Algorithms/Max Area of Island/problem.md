<!-- meta:start -->
# 695. Max Area of Island

**LeetCode:** [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

In a grid of 0s (water) and 1s (land), an island is a group of 1s connected horizontally or vertically. Return the number of cells in the largest island, or 0 if there is no land.

## Input

- `grid`: `m × n` list of lists of the integers 0 and 1

## Output

- The area of the largest island.

## Constraints

- 1 ≤ m, n ≤ 50
- Each cell is 0 or 1

## Edge cases

- No land
- Diagonal neighbours are not connected
- Several islands of the same size

## Examples

| Input | Output | Why |
|---|---|---|
| `[[1, 1, 0], [0, 1, 0], [1, 0, 1]]` | `3` | the top-left island has 3 cells |
| `[[0, 0]]` | `0` | no land |
| `[[1, 0], [0, 1]]` | `1` | two separate single cells |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Graphs · Array · Depth-First Search · Breadth-First Search · Union-Find · Matrix
</details>
<!-- topics:end -->
