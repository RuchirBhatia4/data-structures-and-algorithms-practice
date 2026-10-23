<!-- meta:start -->
# 1. Two Sum

**LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given a list of integers and a target value, find the two **different positions** whose values add up to the target and return those two indices. Exactly one such pair exists, and an element cannot be paired with itself.

## Input

- `nums`: list of integers
- `target`: integer

## Output

- A list `[i, j]` of the two indices (in either order) with `nums[i] + nums[j] == target` and `i != j`.

## Constraints

- 2 ≤ `len(nums)` ≤ 10⁴
- −10⁹ ≤ `nums[i]`, `target` ≤ 10⁹
- Exactly one valid pair exists
- Follow-up: do better than O(n²) time

## Edge cases

- The same value appearing twice (`[6, 6]`, target 12)
- Negative numbers and zero
- The pair uses the last element
- A value equal to `target / 2` that appears only once must not pair with itself

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [2, 11, 5, 15], target = 16` | `[1, 2]` | 11 + 5 = 16 |
| `nums = [-3, 7, 0, 4], target = -3` | `[0, 2]` | −3 + 0 = −3 |
| `nums = [6, 6], target = 12` | `[0, 1]` | two different positions with equal values |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table
</details>
<!-- topics:end -->
