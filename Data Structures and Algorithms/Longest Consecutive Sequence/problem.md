<!-- meta:start -->
# 128. Longest Consecutive Sequence

**LeetCode:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Find the length of the longest run of consecutive integers (x, x+1, x+2, …) whose values all appear in the list. The values can be in any order in the input. The intended solution runs in linear time.

## Input

- `nums`: unsorted list of integers, possibly with duplicates

## Output

- The length of the longest consecutive run (0 for an empty list).

## Constraints

- 0 ≤ `len(nums)` ≤ 10⁵
- −10⁹ ≤ `nums[i]` ≤ 10⁹
- Required: O(n) time

## Edge cases

- Empty list
- Duplicates inside a run
- Negative numbers crossing zero
- Several separate runs

## Examples

| Input | Output | Why |
|---|---|---|
| `[10, 4, 20, 3, 5, 2]` | `4` | 2, 3, 4, 5 |
| `[]` | `0` | no values |
| `[0, -1, 1, 1]` | `3` | −1, 0, 1; the duplicate 1 does not extend the run |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Union-Find
</details>
<!-- topics:end -->
