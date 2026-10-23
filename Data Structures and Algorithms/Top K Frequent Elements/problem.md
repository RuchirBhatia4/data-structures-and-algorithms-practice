<!-- meta:start -->
# 347. Top K Frequent Elements

**LeetCode:** [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the `k` values that occur most often in the list. The input guarantees the answer is unique, and the values may be returned in any order.

## Input

- `nums`: list of integers
- `k`: how many values to return

## Output

- A list of the `k` most frequent values.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁵
- −10⁴ ≤ `nums[i]` ≤ 10⁴
- 1 ≤ `k` ≤ number of distinct values
- The answer is unique
- Follow-up: better than O(n log n) time

## Edge cases

- `k` equals the number of distinct values
- Single element
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [4, 4, 4, 6, 6, 9], k = 2` | `[4, 6]` | 4 appears 3 times, 6 twice, 9 once |
| `nums = [3, 1, 3, 2, 1, 3], k = 1` | `[3]` | 3 appears 3 times |
| `nums = [8], k = 1` | `[8]` | only one value |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Divide and Conquer · Sorting · Heap (Priority Queue) · Bucket Sort · Counting · Quickselect
</details>
<!-- topics:end -->
