<!-- meta:start -->
# 48. Rotate Image

**LeetCode:** [48. Rotate Image](https://leetcode.com/problems/rotate-image/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Rotate an `n × n` matrix 90 degrees clockwise **in place**, without allocating a second matrix.

## Input

- `matrix`: `n × n` list of lists of integers (modified in place)

## Output

- Nothing is returned; the matrix is rotated.

## Constraints

- 1 ≤ n ≤ 20
- −1000 ≤ `matrix[i][j]` ≤ 1000

## Edge cases

- 1 × 1 matrix
- Even and odd `n`
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `[[1, 2], [3, 4]]` | `[[3, 1], [4, 2]]` | the left column becomes the top row |
| `[[5]]` | `[[5]]` | unchanged |
| `[[2, 4, 6], [8, 10, 12], [14, 16, 18]]` | `[[14, 8, 2], [16, 10, 4], [18, 12, 6]]` | 3 × 3 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Math & Geometry · Array · Math · Matrix
</details>
<!-- topics:end -->
