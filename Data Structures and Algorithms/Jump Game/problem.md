<!-- meta:start -->
# 55. Jump Game

**LeetCode:** [55. Jump Game](https://leetcode.com/problems/jump-game/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

You start at index 0, and `nums[i]` is the farthest you may jump forward from index `i` (any shorter jump is also allowed). Decide whether the last index can be reached.

## Input

- `nums`: list of non-negative integers

## Output

- `True` if the last index is reachable, otherwise `False`.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁴
- 0 ≤ `nums[i]` ≤ 10⁵

## Edge cases

- Single element (already there)
- A zero you must jump over
- A zero you cannot get past

## Examples

| Input | Output | Why |
|---|---|---|
| `[2, 0, 1, 0]` | `True` | 0 → 2 → 3 |
| `[1, 0, 2]` | `False` | stuck on the 0 at index 1 |
| `[0]` | `True` | already at the end |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Greedy · Array · Dynamic Programming
</details>
<!-- topics:end -->
