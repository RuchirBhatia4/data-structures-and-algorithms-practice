<!-- meta:start -->
# 349. Intersection of Two Arrays

**LeetCode:** [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the distinct values that appear in both lists. Each value appears once in the result, in any order.

## Input

- `nums1`, `nums2`: lists of integers

## Output

- A list of the unique values present in both inputs.

## Constraints

- 1 ≤ `len(nums1)`, `len(nums2)` ≤ 1000
- 0 ≤ values ≤ 1000

## Edge cases

- No common values
- Many duplicates of a common value
- One list is a subset of the other

## Examples

| Input | Output | Why |
|---|---|---|
| `nums1 = [3, 1, 3, 8], nums2 = [8, 3, 3]` | `[3, 8]` | each common value once |
| `nums1 = [1, 2], nums2 = [4, 5]` | `[]` | nothing in common |
| `nums1 = [6, 6], nums2 = [6]` | `[6]` | duplicates collapse |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Two Pointers · Binary Search · Sorting
</details>
<!-- topics:end -->
