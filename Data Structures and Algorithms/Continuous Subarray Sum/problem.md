<!-- meta:start -->
# 523. Continuous Subarray Sum

**LeetCode:** [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether the list has a contiguous block of **at least two** elements whose sum is a multiple of `k` (zero counts as a multiple of every `k`).

## Input

- `nums`: list of non-negative integers
- `k`: positive integer

## Output

- `True` if such a block exists, otherwise `False`.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁵
- 0 ≤ `nums[i]` ≤ 10⁹
- The total sum fits in a 32-bit signed integer
- 1 ≤ `k` ≤ 2³¹ − 1

## Edge cases

- Two adjacent zeros (sum 0 is a multiple of any `k`)
- A single element that is a multiple of `k` (too short)
- `k = 1`
- `k` larger than every possible sum

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [5, 2, 4], k = 6` | `True` | 2 + 4 = 6 |
| `nums = [5, 2, 4], k = 10` | `False` | block sums are 7, 6 and 11 |
| `nums = [0, 0], k = 7` | `True` | 0 is a multiple of 7 |
| `nums = [9], k = 3` | `False` | needs at least two elements |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Math · Prefix Sum · Pigeonhole Principle
</details>
<!-- topics:end -->
