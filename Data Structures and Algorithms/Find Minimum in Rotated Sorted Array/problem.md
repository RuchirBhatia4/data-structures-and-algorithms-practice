<!-- meta:start -->
# 153. Find Minimum in Rotated Sorted Array

**LeetCode:** [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A list of distinct integers was sorted ascending and then rotated between 1 and n times. Return the smallest value in O(log n) time.

## Input

- `nums`: rotated sorted list of distinct integers

## Output

- The minimum value.

## Constraints

- 1 ≤ n ≤ 5000
- −5000 ≤ `nums[i]` ≤ 5000
- All values are distinct
- Required: O(log n) time

## Edge cases

- Rotated n times (looks unrotated)
- Two elements
- Single element
- Minimum at the last position

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 6, 1, 2, 3, 4]` | `1` | rotation point |
| `[2, 3, 4, 5]` | `2` | fully rotated back |
| `[9, 4]` | `4` | two elements |
| `[7]` | `7` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Binary Search · Array
</details>
<!-- topics:end -->
