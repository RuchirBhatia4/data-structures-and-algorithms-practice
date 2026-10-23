<!-- meta:start -->
# 215. Kth Largest Element in an Array

**LeetCode:** [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the `k`-th largest value in the list, counting duplicates (the `k`-th element if the list were sorted in descending order, not the `k`-th distinct value). The statement asks whether it can be done without sorting.

## Input

- `nums`: list of integers
- `k`: rank from the top

## Output

- The `k`-th largest value.

## Constraints

- 1 ≤ `k` ≤ `len(nums)` ≤ 10⁵
- −10⁴ ≤ `nums[i]` ≤ 10⁴

## Edge cases

- Duplicates of the answer
- `k = 1` or `k = len(nums)`
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [7, 2, 9, 4], k = 2` | `7` | descending order is 9, 7, 4, 2 |
| `nums = [5, 5, 1], k = 2` | `5` | duplicates count separately |
| `nums = [-3], k = 1` | `-3` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Heap / Priority Queue · Array · Divide and Conquer · Sorting · Heap (Priority Queue) · Quickselect
</details>
<!-- topics:end -->
