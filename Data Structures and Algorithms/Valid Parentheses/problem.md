<!-- meta:start -->
# 20. Valid Parentheses

**LeetCode:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A string contains only the brackets `()`, `[]` and `{}`. It is valid when every opening bracket is closed by the same type of bracket, brackets close in the correct order, and every closing bracket has a matching opener.

## Input

- `s`: string of bracket characters

## Output

- `True` if the brackets are balanced and properly nested, otherwise `False`.

## Constraints

- 1 ≤ `len(s)` ≤ 10⁴
- Only the characters `()[]{}`

## Edge cases

- Only opening brackets
- Starts with a closing bracket
- Interleaved types such as `[(])`
- Odd length

## Examples

| Input | Output | Why |
|---|---|---|
| `"{[]}()"` | `True` | properly nested |
| `"[(])"` | `False` | closed in the wrong order |
| `"(("` | `False` | never closed |
| `"}{"` | `False` | closer without an opener |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · String · Bracket Sequences
</details>
<!-- topics:end -->
