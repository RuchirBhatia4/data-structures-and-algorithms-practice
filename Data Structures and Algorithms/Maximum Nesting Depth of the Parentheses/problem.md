<!-- meta:start -->
# 1614. Maximum Nesting Depth of the Parentheses

**LeetCode:** [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The string is a valid parentheses expression that may also contain digits and `+ - * /`. Return the largest number of parentheses that are open at the same time.

## Input

- `s`: valid parentheses expression

## Output

- The maximum nesting depth (0 if there are no parentheses).

## Constraints

- 1 ≤ `len(s)` ≤ 100
- Digits, `+ - * /` and parentheses only
- The parentheses are always balanced

## Edge cases

- No parentheses
- Several groups side by side
- Deep nesting with digits between levels

## Examples

| Input | Output | Why |
|---|---|---|
| `"(1+(2*3))"` | `2` | the inner group is two levels deep |
| `"8"` | `0` | no parentheses |
| `"((5))+(6)"` | `2` | the first group is two deep |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · String · Bracket Sequences
</details>
<!-- topics:end -->
