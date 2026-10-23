<!-- meta:start -->
# 49. Group Anagrams

**LeetCode:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given a list of words, put words that are anagrams of each other (same letters, same counts) into the same group. Groups and the words inside them may be returned in any order.

## Input

- `strs`: list of lowercase strings (possibly empty strings)

## Output

- A list of groups, each group a list of words that are anagrams of one another.

## Constraints

- 1 ≤ `len(strs)` ≤ 10⁴
- 0 ≤ `len(strs[i])` ≤ 100
- Lowercase English letters only

## Edge cases

- Empty strings (all empty strings belong together)
- A single word
- No two words are anagrams
- Words with repeated letters (`aab` vs `abb` are different)

## Examples

| Input | Output | Why |
|---|---|---|
| `["dusty", "study", "night", "thing", "act"]` | `[["dusty", "study"], ["night", "thing"], ["act"]]` | each group shares the same letters |
| `["", ""]` | `[["", ""]]` | empty strings are anagrams of each other |
| `["x"]` | `[["x"]]` | one word forms one group |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · Hash Table · String · Sorting
</details>
<!-- topics:end -->
