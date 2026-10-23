<!-- meta:start -->
# 5. Longest Palindromic Substring

**LeetCode:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the longest contiguous substring that reads the same forwards and backwards. If several have the maximum length, any one of them is accepted.

## Input

- `s`: string of digits and English letters

## Output

- A longest palindromic substring.

## Constraints

- 1 ≤ `len(s)` ≤ 1000
- Digits and English letters only

## Edge cases

- Even-length palindromes
- No repeated characters (any single character)
- The whole string is a palindrome

## Examples

| Input | Output | Why |
|---|---|---|
| `"xabbay"` | `"abba"` | even length |
| `"racecars"` | `"racecar"` | odd length |
| `"abc"` | `"a"`, `"b"` or `"c"` | length 1 ties |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Dynamic Programming · Two Pointers · String · Manacher
</details>
<!-- topics:end -->
