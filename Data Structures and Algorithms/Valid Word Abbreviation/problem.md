<!-- meta:start -->
# 408. Valid Word Abbreviation

**LeetCode:** [408. Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) · **Difficulty:** Easy · LeetCode Premium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

An abbreviation replaces some non-adjacent, non-empty substrings of a word with their lengths (numbers have no leading zeros). Given a word and an abbreviation, decide whether the abbreviation describes the word exactly.

## Input

- `word`: lowercase string
- `abbr`: string of lowercase letters and digits

## Output

- `True` if `abbr` is a valid abbreviation of `word`, otherwise `False`.

## Constraints

- Short strings (tens of characters)
- Numbers in `abbr` fit in a 32-bit integer
- _Exact limits: see the official problem._

## Edge cases

- A number with a leading zero (invalid)
- Abbreviation that is only a number
- Total length too short or too long
- Multi-digit numbers

## Examples

| Input | Output | Why |
|---|---|---|
| `word = "kitten", abbr = "k4n"` | `True` | k + 4 letters + n |
| `word = "kitten", abbr = "k3n"` | `False` | covers only 5 letters |
| `word = "kitten", abbr = "k04n"` | `False` | leading zero |
| `word = "cat", abbr = "3"` | `True` | the whole word |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Two Pointers · String
</details>
<!-- topics:end -->
