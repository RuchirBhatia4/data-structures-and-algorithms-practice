<!-- meta:start -->
# 200. Number of Islands

**LeetCode:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The grid is a map of `'1'` (land) and `'0'` (water). An island is a group of land cells connected horizontally or vertically, and everything outside the grid is water. Count the islands.

## Input

- `grid`: `m × n` list of lists of the strings `'0'` and `'1'`

## Output

- The number of islands.

## Constraints

- 1 ≤ m, n ≤ 300
- Each cell is `'0'` or `'1'`

## Edge cases

- Diagonal neighbours are not connected
- No land at all
- One island covering the whole grid
- Islands with holes

## Examples

| Input | Output | Why |
|---|---|---|
| `[["1","0","1"], ["0","0","0"], ["1","1","0"]]` | `3` | two single cells and one pair |
| `[["0"]]` | `0` | no land |
| `[["1","0"], ["0","1"]]` | `2` | diagonals do not connect |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Graphs · Array · Depth-First Search · Breadth-First Search · Union-Find · Matrix
</details>
<!-- topics:end -->
