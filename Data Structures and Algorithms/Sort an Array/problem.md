<!-- meta:start -->
# 912. Sort an Array

**LeetCode:** [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Sort a list of integers in ascending order **without** using built-in sorting functions, in O(n log n) time and with as little extra space as possible.

## Input

- `nums`: list of integers

## Output

- The sorted list.

## Constraints

- 1 ≤ `len(nums)` ≤ 5 × 10⁴
- −5 × 10⁴ ≤ `nums[i]` ≤ 5 × 10⁴
- No built-in sort; O(n log n) time

## Edge cases

- Duplicates
- Already sorted or reverse sorted input
- Negative values
- Single element

## Examples

| Input | Output | Why |
|---|---|---|
| `[3, -1, 2]` | `[-1, 2, 3]` | ascending |
| `[4, 4, 1]` | `[1, 4, 4]` | duplicates kept |
| `[0]` | `[0]` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sorting · Array · Divide and Conquer · Heap (Priority Queue) · Merge Sort · Bucket Sort · Radix Sort · Counting Sort
</details>
<!-- topics:end -->
