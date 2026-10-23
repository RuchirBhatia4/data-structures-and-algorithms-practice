<!-- meta:start -->
# 125. Valid Palindrome

**LeetCode:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Lowercase the string and drop everything that is not a letter or digit. Decide whether what is left reads the same forwards and backwards.

## Input

- `s`: string of printable ASCII characters

## Output

- `True` if the cleaned string is a palindrome, otherwise `False`.

## Constraints

- 1 ≤ `len(s)` ≤ 2 × 10⁵
- Printable ASCII characters

## Edge cases

- No letters or digits at all (empty after cleaning, so `True`)
- Digits mixed with letters
- Upper/lower case of the same letter
- Punctuation between matching letters

## Examples

| Input | Output | Why |
|---|---|---|
| `"No 'x' in Nixon"` | `True` | "noxinnixon" reversed is the same |
| `"ab_a"` | `True` | "aba" |
| `"1a2"` | `False` | 1 ≠ 2 |
| `".,!"` | `True` | nothing left to compare |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Two Pointers · String
</details>
<!-- topics:end -->
