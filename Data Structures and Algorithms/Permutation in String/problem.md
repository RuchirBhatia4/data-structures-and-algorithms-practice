<!-- meta:start -->
# 567. Permutation in String

**LeetCode:** [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether some rearrangement of `s1` appears as a contiguous substring of `s2`.

## Input

- `s1`: lowercase string
- `s2`: lowercase string to search in

## Output

- `True` if a permutation of `s1` occurs in `s2`, otherwise `False`.

## Constraints

- 1 ≤ `len(s1)`, `len(s2)` ≤ 10⁴
- Lowercase English letters only

## Edge cases

- `s1` longer than `s2`
- Repeated letters in `s1`
- Match at the very end of `s2`
- Same letters present but not contiguous

## Examples

| Input | Output | Why |
|---|---|---|
| `s1 = "ab", s2 = "xbay"` | `True` | "ba" is a permutation of "ab" |
| `s1 = "aab", s2 = "abab"` | `True` | "aba" |
| `s1 = "aab", s2 = "abba"` | `False` | every length-3 window has two b's |
| `s1 = "abcd", s2 = "abc"` | `False` | `s1` is longer |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sliding Window · Hash Table · Two Pointers · String
</details>
<!-- topics:end -->
