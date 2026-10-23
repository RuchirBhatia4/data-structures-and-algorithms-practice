<!-- meta:start -->
# 136. Single Number

**LeetCode:** [136. Single Number](https://leetcode.com/problems/single-number/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Every value in the list appears exactly twice except one, which appears once. Find that value in linear time with constant extra space.

## Input

- `nums`: list of integers

## Output

- The value that appears once.

## Constraints

- 1 ≤ `len(nums)` ≤ 3 × 10⁴
- −3 × 10⁴ ≤ `nums[i]` ≤ 3 × 10⁴
- Exactly one value appears once; all others twice
- Required: O(n) time, O(1) extra space

## Edge cases

- Single element
- Negative numbers
- The lone value at either end

## Examples

| Input | Output | Why |
|---|---|---|
| `[8, 3, 8]` | `3` | 8 appears twice |
| `[-1]` | `-1` | single element |
| `[6, 9, 9, 7, 6]` | `7` | 6 and 9 are paired |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Array
</details>
<!-- topics:end -->
