<!-- meta:start -->
# 2965. Find Missing and Repeated Values

**LeetCode:** [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

An `n × n` grid should contain each number from 1 to n² exactly once, but one number `a` appears twice and one number `b` is missing. Return `[a, b]`.

## Input

- `grid`: `n × n` list of lists of integers

## Output

- `[a, b]` where `a` is the repeated value and `b` the missing value.

## Constraints

- 2 ≤ `n` ≤ 50
- 1 ≤ `grid[i][j]` ≤ n²
- Exactly one value repeats and exactly one is missing

## Edge cases

- Missing value is 1 or n²
- Repeated values in different rows
- Smallest grid (n = 2)

## Examples

| Input | Output | Why |
|---|---|---|
| `[[1, 3], [3, 4]]` | `[3, 2]` | 3 twice, 2 missing |
| `[[4, 1], [2, 1]]` | `[1, 3]` | 1 twice, 3 missing |
| `[[9, 1, 7], [8, 9, 2], [3, 4, 6]]` | `[9, 5]` | 9 twice, 5 missing |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Math · Matrix
</details>
<!-- topics:end -->
