<!-- meta:start -->
# 15. 3Sum

**LeetCode:** [15. 3Sum](https://leetcode.com/problems/3sum/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Find every distinct triplet of values taken from three different positions whose sum is zero. The result must not contain the same triplet twice; triplets and their order can be returned in any order.

## Input

- `nums`: list of integers

## Output

- A list of triplets `[a, b, c]` with `a + b + c == 0`, without duplicates.

## Constraints

- 3 ≤ `len(nums)` ≤ 3000
- −10⁵ ≤ `nums[i]` ≤ 10⁵

## Edge cases

- Many zeros (only one `[0, 0, 0]`)
- No valid triplet
- Repeated values that would create duplicate triplets

## Examples

| Input | Output | Why |
|---|---|---|
| `[-2, 0, 1, 1, 2]` | `[[-2, 0, 2], [-2, 1, 1]]` | two distinct triplets |
| `[1, 2, 3]` | `[]` | all positive |
| `[0, 0, 0, 0]` | `[[0, 0, 0]]` | reported once |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Two Pointers · Array · Sorting
</details>
<!-- topics:end -->
