<!-- meta:start -->
# 45. Jump Game II

**LeetCode:** [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

You start at index 0, and `nums[i]` is the farthest you may jump forward from index `i`. Reaching the last index is always possible. Return the minimum number of jumps needed.

## Input

- `nums`: list of non-negative integers

## Output

- The minimum number of jumps to reach the last index.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁴
- 0 ≤ `nums[i]` ≤ 1000
- The last index is always reachable

## Edge cases

- Single element (0 jumps)
- One jump covers everything
- The longest jump is not always the best first jump

## Examples

| Input | Output | Why |
|---|---|---|
| `[1, 3, 1, 1, 1]` | `2` | 0 → 1 → 4 |
| `[0]` | `0` | already at the end |
| `[2, 1, 1]` | `1` | jump straight to index 2 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Greedy · Array · Dynamic Programming
</details>
<!-- topics:end -->
