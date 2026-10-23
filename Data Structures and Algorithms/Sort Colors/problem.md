<!-- meta:start -->
# 75. Sort Colors

**LeetCode:** [75. Sort Colors](https://leetcode.com/problems/sort-colors/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The list contains only 0s, 1s and 2s (three colours). Rearrange it **in place** so that all 0s come first, then all 1s, then all 2s, without using a library sort.

## Input

- `nums`: list of 0s, 1s and 2s (modified in place)

## Output

- Nothing is returned; `nums` ends up sorted.

## Constraints

- 1 ≤ `len(nums)` ≤ 300
- Each value is 0, 1 or 2
- Follow-up: a single pass with constant extra space

## Edge cases

- Only one colour present
- Already sorted
- Sorted in reverse
- Single element

## Examples

| Input | Output | Why |
|---|---|---|
| `[2, 1, 0, 2, 0]` | `[0, 0, 1, 2, 2]` | grouped by colour |
| `[1]` | `[1]` | single element |
| `[2, 2, 0]` | `[0, 2, 2]` | no 1s |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Two Pointers · Sorting · Quicksort · Bubble Sort
</details>
<!-- topics:end -->
