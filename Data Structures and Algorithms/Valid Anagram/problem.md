<!-- meta:start -->
# 242. Valid Anagram

**LeetCode:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether string `t` is a rearrangement of string `s`: both must use exactly the same letters with exactly the same number of occurrences.

## Input

- `s`, `t`: strings of lowercase English letters

## Output

- `True` if `t` is an anagram of `s`, otherwise `False`.

## Constraints

- 1 ≤ `len(s)`, `len(t)` ≤ 5 × 10⁴
- Lowercase English letters only
- Follow-up: how would the approach change for arbitrary Unicode characters?

## Edge cases

- Different lengths
- Same set of letters but different counts
- Identical strings
- Single characters

## Examples

| Input | Output | Why |
|---|---|---|
| `s = "stressed", t = "desserts"` | `True` | same letters, same counts |
| `s = "aab", t = "abb"` | `False` | `a` appears twice in `s` but once in `t` |
| `s = "ab", t = "abc"` | `False` | different lengths |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Hash Table · String · Sorting
</details>
<!-- topics:end -->
