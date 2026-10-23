<!-- meta:start -->
# 167. Two Sum II - Input Array Is Sorted

**LeetCode:** [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The list is sorted in non-decreasing order. Find the two different positions whose values add up to the target and return them as **1-based** indices with the smaller index first. Exactly one answer exists, and only constant extra space may be used.

## Input

- `numbers`: sorted list of integers
- `target`: integer

## Output

- `[i, j]` with 1 ≤ i < j and `numbers[i-1] + numbers[j-1] == target`.

## Constraints

- 2 ≤ `len(numbers)` ≤ 3 × 10⁴
- −1000 ≤ `numbers[i]`, `target` ≤ 1000
- Exactly one solution
- Required: O(1) extra space

## Edge cases

- Negative numbers
- Equal values forming the pair
- Pair at the two ends

## Examples

| Input | Output | Why |
|---|---|---|
| `numbers = [1, 3, 4, 8], target = 12` | `[3, 4]` | 4 + 8 (1-based positions 3 and 4) |
| `numbers = [-5, -2, 0, 7], target = -7` | `[1, 2]` | −5 + −2 |
| `numbers = [2, 2, 3], target = 4` | `[1, 2]` | two equal values |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Two Pointers · Array · Binary Search
</details>
<!-- topics:end -->
