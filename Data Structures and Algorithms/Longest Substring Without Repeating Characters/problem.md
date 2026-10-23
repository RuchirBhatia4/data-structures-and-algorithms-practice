<!-- meta:start -->
# 3. Longest Substring Without Repeating Characters

**LeetCode:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Find the length of the longest contiguous piece of the string in which no character appears twice.

## Input

- `s`: string of English letters, digits, symbols and spaces

## Output

- The length of the longest substring with all distinct characters.

## Constraints

- 0 ≤ `len(s)` ≤ 10⁵
- English letters, digits, symbols and spaces

## Edge cases

- Empty string
- All characters the same
- Spaces count as characters
- A repeated character far back that should not shrink the answer

## Examples

| Input | Output | Why |
|---|---|---|
| `"tmmzuxt"` | `5` | "mzuxt" |
| `""` | `0` | empty string |
| `"aaaa"` | `1` | "a" |
| `"a b"` | `3` | the space is a distinct character |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sliding Window · Hash Table · String
</details>
<!-- topics:end -->
