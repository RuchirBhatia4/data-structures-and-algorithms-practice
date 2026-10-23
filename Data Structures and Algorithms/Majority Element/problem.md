<!-- meta:start -->
# 169. Majority Element

**LeetCode:** [169. Majority Element](https://leetcode.com/problems/majority-element/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the value that appears more than half the time (more than ⌊n / 2⌋ times). Such a value is guaranteed to exist.

## Input

- `nums`: list of integers

## Output

- The majority value.

## Constraints

- 1 ≤ `len(nums)` ≤ 5 × 10⁴
- −10⁹ ≤ `nums[i]` ≤ 10⁹
- A majority value always exists
- Follow-up: linear time and O(1) extra space

## Edge cases

- Single element
- Majority value not in the first position
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 1, 5]` | `5` | 2 of 3 |
| `[2, 2, 1, 1, 2]` | `2` | 3 of 5 |
| `[-4]` | `-4` | single element |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Divide and Conquer · Sorting · Counting · Boyer–Moore Majority Vote Algorithm
</details>
<!-- topics:end -->
