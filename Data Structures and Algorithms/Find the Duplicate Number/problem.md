<!-- meta:start -->
# 287. Find the Duplicate Number

**LeetCode:** [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A list of `n + 1` integers contains only values from 1 to `n`, and exactly one value occurs more than once (it may occur many times). Return that value **without modifying the list** and using only constant extra space.

## Input

- `nums`: list of `n + 1` integers in the range [1, n]

## Output

- The repeated value.

## Constraints

- 1 ≤ n ≤ 10⁵
- `len(nums) == n + 1`
- 1 ≤ `nums[i]` ≤ n
- Exactly one value repeats (two or more times)
- Required: do not modify `nums`; O(1) extra space
- Follow-up: prove a duplicate must exist; solve in linear time

## Edge cases

- The duplicate appears more than twice
- Smallest case `[1, 1]`
- Duplicate is the largest value

## Examples

| Input | Output | Why |
|---|---|---|
| `[1, 4, 2, 4, 3]` | `4` | 4 appears twice |
| `[2, 2, 2]` | `2` | appears three times |
| `[3, 1, 3, 2]` | `3` | 3 appears twice |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Array · Two Pointers · Binary Search · Bit Manipulation · Pigeonhole Principle · Floyd's Cycle Finding Algorithm
</details>
<!-- topics:end -->
