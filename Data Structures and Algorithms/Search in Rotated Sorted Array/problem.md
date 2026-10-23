<!-- meta:start -->
# 33. Search in Rotated Sorted Array

**LeetCode:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A list of distinct integers was sorted ascending and then possibly rotated at an unknown point (for example `[1, 2, 4, 6, 7]` might become `[6, 7, 1, 2, 4]`). Return the index of `target`, or −1 if it is absent. The required running time is O(log n).

## Input

- `nums`: rotated sorted list of distinct integers
- `target`: integer to find

## Output

- The index of `target`, or −1.

## Constraints

- 1 ≤ `len(nums)` ≤ 5000
- −10⁴ ≤ `nums[i]`, `target` ≤ 10⁴
- All values are distinct
- Required: O(log n) time

## Edge cases

- Not rotated at all
- Single element
- Target at the rotation point
- Target absent

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [6, 7, 1, 2, 4], target = 2` | `3` | found after the rotation point |
| `nums = [6, 7, 1, 2, 4], target = 5` | `-1` | absent |
| `nums = [3], target = 3` | `0` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Binary Search · Array
</details>
<!-- topics:end -->
