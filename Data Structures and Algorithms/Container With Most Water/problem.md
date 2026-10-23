<!-- meta:start -->
# 11. Container With Most Water

**LeetCode:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Each value is the height of a vertical line at that x-position. Two lines and the x-axis form a container that holds `min(height[i], height[j]) × (j − i)` water. Return the largest amount any pair of lines can hold.

## Input

- `height`: list of non-negative integers

## Output

- The maximum water area.

## Constraints

- 2 ≤ `len(height)` ≤ 10⁵
- 0 ≤ `height[i]` ≤ 10⁴

## Edge cases

- Only two lines
- Zero heights
- Tallest lines adjacent vs. shorter lines far apart

## Examples

| Input | Output | Why |
|---|---|---|
| `[2, 5, 4, 3]` | `6` | lines 0 and 3 (2 × 3) or lines 1 and 3 (3 × 2) |
| `[3, 3]` | `3` | 3 × 1 |
| `[0, 7, 0]` | `0` | every pair includes a zero-height line |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Two Pointers · Array · Greedy
</details>
<!-- topics:end -->
