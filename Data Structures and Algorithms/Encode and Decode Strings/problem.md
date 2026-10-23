<!-- meta:start -->
# 271. Encode and Decode Strings

**LeetCode:** [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) · **Difficulty:** Medium · LeetCode Premium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Design two functions: one turns a list of strings into a single string, and the other turns that single string back into the original list. Decoding the encoded value must reproduce the list exactly, for any strings, including empty strings and strings that contain whatever delimiter you might choose.

## Input

- `encode(strs)`: `strs` is a list of strings
- `decode(s)`: `s` is a string produced by `encode`

## Output

- `encode` returns one string
- `decode` returns the original list of strings

## Constraints

- A few hundred strings of up to a few hundred characters each
- Strings may contain any ASCII character
- _Exact limits: see the official problem._

## Edge cases

- Empty list
- List containing empty strings
- Strings containing digits and the delimiter character
- Very long strings

## Examples

| Input | Output | Why |
|---|---|---|
| `["hi", "there"]` | `["hi", "there"]` | round trip |
| `["", "a#b"]` | `["", "a#b"]` | empty string and a delimiter-like character survive |
| `[]` | `[]` | empty list survives |

> Examples show `decode(encode(x))`. NeetCode's version puts both methods on `Solution`; LeetCode uses a `Codec` class.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Array · String · Design
</details>
<!-- topics:end -->
