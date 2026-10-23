<!-- meta:start -->
# 53. Maximum Subarray

**LeetCode:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Find the largest possible sum of a non-empty contiguous block of the list.

## Input

- `nums`: list of integers

## Output

- The maximum block sum.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁵
- −10⁴ ≤ `nums[i]` ≤ 10⁴
- Follow-up: after the linear-time solution, try a divide-and-conquer one

## Edge cases

- All negative numbers (the answer is the largest single value)
- Single element
- Best block in the middle

## Examples

| Input | Output | Why |
|---|---|---|
| `[3, -4, 5, -1, 2]` | `6` | 5 − 1 + 2 |
| `[-7, -2, -9]` | `-2` | single best element |
| `[4]` | `4` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Greedy · Array · Divide and Conquer · Dynamic Programming
</details>
<!-- topics:end -->
