<!-- meta:start -->
# 66. Plus One

**LeetCode:** [66. Plus One](https://leetcode.com/problems/plus-one/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A large non-negative integer is stored as a list of its digits, most significant first. Add one and return the new list of digits.

## Input

- `digits`: list of digits with no leading zero

## Output

- The digits of the number plus one.

## Constraints

- 1 ≤ `len(digits)` ≤ 100
- 0 ≤ `digits[i]` ≤ 9
- No leading zeros

## Edge cases

- Trailing 9s that carry
- All 9s (the list grows)
- Single digit

## Examples

| Input | Output | Why |
|---|---|---|
| `[4, 5]` | `[4, 6]` | no carry |
| `[1, 9, 9]` | `[2, 0, 0]` | carry ripples |
| `[9]` | `[1, 0]` | one more digit |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Math & Geometry · Array · Math
</details>
<!-- topics:end -->
