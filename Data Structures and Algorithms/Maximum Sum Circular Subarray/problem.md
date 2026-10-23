<!-- meta:start -->
# 918. Maximum Sum Circular Subarray

**LeetCode:** [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The list is circular: after the last element comes the first one again. Find the largest sum of a non-empty contiguous block, where a block may wrap around the end but may not use any element twice.

## Input

- `nums`: list of integers, viewed as a circle

## Output

- The maximum circular block sum.

## Constraints

- 1 ≤ n ≤ 3 × 10⁴
- −3 × 10⁴ ≤ `nums[i]` ≤ 3 × 10⁴

## Edge cases

- All negative numbers
- The best block wraps around
- The whole list is the best block

## Examples

| Input | Output | Why |
|---|---|---|
| `[6, -10, 4]` | `10` | 4 then wrap to 6 |
| `[-3, -1]` | `-1` | single best element |
| `[2, -1, 2]` | `4` | the last 2, then wrap to the first 2 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Greedy · Array · Divide and Conquer · Dynamic Programming · Queue · Monotonic Queue
</details>
<!-- topics:end -->
