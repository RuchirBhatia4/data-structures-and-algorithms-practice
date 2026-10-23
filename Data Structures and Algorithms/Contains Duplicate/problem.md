<!-- meta:start -->
# 217. Contains Duplicate

**LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Report whether any value occurs at least twice in the list.

## Input

- `nums`: list of integers

## Output

- `True` if some value appears two or more times, otherwise `False`.

## Constraints

- 1 ≤ `len(nums)` ≤ 10⁵
- −10⁹ ≤ `nums[i]` ≤ 10⁹

## Edge cases

- Single element
- Duplicate values far apart
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `[7, 1, 7]` | `True` | 7 appears twice |
| `[1, 2, 3, 4]` | `False` | all values distinct |
| `[5]` | `False` | one element cannot repeat |

> NeetCode's version names the method `hasDuplicate`; LeetCode's starter code calls it `containsDuplicate`.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · Sorting
</details>
<!-- topics:end -->
