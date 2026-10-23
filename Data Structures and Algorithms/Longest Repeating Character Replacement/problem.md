<!-- meta:start -->
# 424. Longest Repeating Character Replacement

**LeetCode:** [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

You may change at most `k` characters of an uppercase string into any other uppercase letters. Return the length of the longest substring that can be made of a single repeated letter.

## Input

- `s`: string of uppercase English letters
- `k`: maximum number of replacements

## Output

- The maximum achievable length of a block of identical letters.

## Constraints

- 1 ≤ `len(s)` ≤ 10⁵
- Uppercase English letters only
- 0 ≤ `k` ≤ `len(s)`

## Edge cases

- `k = 0`
- `k` at least the length of the string
- All letters different
- Single character

## Examples

| Input | Output | Why |
|---|---|---|
| `s = "AABCB", k = 1` | `3` | change C in "BCB" (or B in "AAB") |
| `s = "XYZ", k = 0` | `1` | no changes allowed |
| `s = "ABBB", k = 2` | `4` | change the A |
| `s = "Q", k = 1` | `1` | single character |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sliding Window · Hash Table · String
</details>
<!-- topics:end -->
