<!-- meta:start -->
# 150. Evaluate Reverse Polish Notation

**LeetCode:** [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Evaluate an arithmetic expression written in reverse Polish (postfix) notation, where each operator comes after its two operands. Division between integers truncates toward zero. The expression is always valid.

## Input

- `tokens`: list of strings, each an integer or one of `+`, `-`, `*`, `/`

## Output

- The integer value of the expression.

## Constraints

- 1 ≤ `len(tokens)` ≤ 10⁴
- Integers are in [−200, 200]
- The expression is valid and intermediate results fit in 32 bits
- No division by zero

## Edge cases

- A single number
- Negative operands
- Division of a negative number (truncate toward zero, not floor)
- Operand order for `-` and `/`

## Examples

| Input | Output | Why |
|---|---|---|
| `["4", "2", "-", "3", "*"]` | `6` | (4 − 2) × 3 |
| `["7", "-2", "/"]` | `-3` | −3.5 truncated toward zero |
| `["5"]` | `5` | just a number |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · Array · Math
</details>
<!-- topics:end -->
