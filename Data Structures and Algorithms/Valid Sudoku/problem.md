<!-- meta:start -->
# 36. Valid Sudoku

**LeetCode:** [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Check whether a partially filled 9 × 9 Sudoku board breaks any rule. Only the filled cells are checked: no digit may repeat within a row, within a column, or within any of the nine 3 × 3 boxes. The board does not have to be solvable.

## Input

- `board`: 9 × 9 grid of strings, each a digit `'1'`–`'9'` or `'.'` for empty

## Output

- `True` if no rule is broken by the filled cells, otherwise `False`.

## Constraints

- Exactly 9 rows and 9 columns
- Each cell is `'1'`–`'9'` or `'.'`

## Edge cases

- Repeat inside a box but not in any row or column
- Repeat in a column
- An almost empty board
- A valid board that has no solution (still `True`)

## Examples

| Input | Output | Why |
|---|---|---|
| Empty board except `'5'` at (0, 0) and (0, 8) | `False` | same row |
| Empty board except `'5'` at (0, 0) and (2, 2) | `False` | same top-left box |
| Empty board except `'5'` at (0, 0) and (4, 4) | `True` | different row, column and box |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Matrix
</details>
<!-- topics:end -->
