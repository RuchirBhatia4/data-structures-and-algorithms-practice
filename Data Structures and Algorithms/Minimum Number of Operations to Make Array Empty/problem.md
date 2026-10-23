<!-- meta:start -->
# 2870. Minimum Number of Operations to Make Array Empty

**LeetCode:** [2870. Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

One operation deletes either two equal values or three equal values from the list. Return the fewest operations that delete everything, or −1 if that is impossible.

## Input

- `nums`: list of positive integers

## Output

- The minimum number of operations, or −1.

## Constraints

- 2 ≤ `len(nums)` ≤ 10⁵
- 1 ≤ `nums[i]` ≤ 10⁶
- Same problem as LeetCode 2244 (Minimum Rounds to Complete All Tasks)

## Edge cases

- A value that appears exactly once (impossible)
- Counts of 4 and 5
- Large counts

## Examples

| Input | Output | Why |
|---|---|---|
| `[4, 4, 4, 4, 7, 7]` | `3` | four 4s take two pairs; two 7s take one pair |
| `[1, 1, 1, 2]` | `-1` | a single 2 cannot be removed |
| `[5, 5, 5, 5, 5]` | `2` | one triple and one pair |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Greedy · Array · Hash Table · Counting
</details>
<!-- topics:end -->
