<!-- meta:start -->
# 27. Remove Element

**LeetCode:** [27. Remove Element](https://leetcode.com/problems/remove-element/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Remove every occurrence of `val` from `nums` **in place** and return `k`, the number of remaining elements. The first `k` positions must hold the kept values (in any order); whatever is left after them does not matter.

## Input

- `nums`: list of integers (modified in place)
- `val`: value to remove

## Output

- `k`, with `nums[:k]` containing exactly the elements not equal to `val`.

## Constraints

- 0 ≤ `len(nums)` ≤ 100
- 0 ≤ `nums[i]` ≤ 50
- 0 ≤ `val` ≤ 100

## Edge cases

- Empty list
- Every element equals `val`
- `val` not present
- `val` at both ends

## Examples

| Input | Output | Why |
|---|---|---|
| `nums = [4, 1, 4, 2], val = 4` | `2  (nums starts with 1, 2)` | two values remain |
| `nums = [], val = 1` | `0` | nothing to keep |
| `nums = [3, 3], val = 3` | `0` | everything removed |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Two Pointers
</details>
<!-- topics:end -->
