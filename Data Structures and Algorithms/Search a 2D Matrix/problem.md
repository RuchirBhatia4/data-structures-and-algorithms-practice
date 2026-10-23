<!-- meta:start -->
# 74. Search a 2D Matrix

**LeetCode:** [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Each row of the matrix is sorted ascending, and the first value of every row is greater than the last value of the previous row. Decide whether `target` is in the matrix in O(log(m · n)) time.

## Input

- `matrix`: `m × n` list of lists of integers
- `target`: integer

## Output

- `True` if `target` appears in the matrix, otherwise `False`.

## Constraints

- 1 ≤ m, n ≤ 100
- −10⁴ ≤ values, `target` ≤ 10⁴
- Required: O(log(m · n)) time

## Edge cases

- Single cell
- Target smaller than everything or larger than everything
- Target between two rows
- Single row or single column

## Examples

| Input | Output | Why |
|---|---|---|
| `matrix = [[2, 4, 7], [9, 12, 15]], target = 12` | `True` | second row |
| `matrix = [[2, 4, 7], [9, 12, 15]], target = 8` | `False` | falls between the rows |
| `matrix = [[5]], target = 5` | `True` | single cell |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Binary Search · Array · Matrix
</details>
<!-- topics:end -->
