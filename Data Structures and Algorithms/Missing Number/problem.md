<!-- meta:start -->
# 268. Missing Number

**LeetCode:** [268. Missing Number](https://leetcode.com/problems/missing-number/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The list contains `n` distinct numbers taken from the range 0 to `n` (inclusive), so exactly one number in that range is missing. Return it.

## Input

- `nums`: list of `n` distinct integers from [0, n]

## Output

- The missing number.

## Constraints

- 1 ≤ n ≤ 10⁴
- 0 ≤ `nums[i]` ≤ n
- All values distinct
- Follow-up: O(1) extra space and O(n) time

## Edge cases

- 0 is missing
- `n` is missing
- Single element

## Examples

| Input | Output | Why |
|---|---|---|
| `[0, 1, 3]` | `2` | range 0–3 |
| `[1]` | `0` | range 0–1 |
| `[2, 0, 1]` | `3` | range 0–3, the top value is missing |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Array · Hash Table · Math · Binary Search · Sorting
</details>
<!-- topics:end -->
