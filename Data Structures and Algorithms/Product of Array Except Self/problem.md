<!-- meta:start -->
# 238. Product of Array Except Self

**LeetCode:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

For each position `i`, compute the product of every element of the array **except** `nums[i]`. The solution must run in linear time and must not use division.

## Input

- `nums`: list of integers

## Output

- A list `answer` of the same length where `answer[i]` is the product of all elements other than `nums[i]`.

## Constraints

- 2 ≤ `len(nums)` ≤ 10⁵
- −30 ≤ `nums[i]` ≤ 30
- Every answer fits in a 32-bit signed integer
- Required: O(n) time and no division
- Follow-up: O(1) extra space, not counting the output list

## Edge cases

- Exactly one zero (only that position is non-zero)
- Two or more zeros (everything is zero)
- Negative numbers
- Length 2

## Examples

| Input | Output | Why |
|---|---|---|
| `[2, 3, 4]` | `[12, 8, 6]` | 3·4, 2·4, 2·3 |
| `[5, 0, 2]` | `[0, 10, 0]` | only the position of the zero avoids multiplying by zero |
| `[-1, 2, 0, 0]` | `[0, 0, 0, 0]` | two zeros make every product zero |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Prefix Sum
</details>
<!-- topics:end -->
