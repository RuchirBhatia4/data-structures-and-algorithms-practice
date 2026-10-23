<!-- meta:start -->
# 371. Sum of Two Integers

**LeetCode:** [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the sum of two integers **without** using the `+` or `-` operators.

## Input

- `a`, `b`: integers

## Output

- `a + b`.

## Constraints

- −1000 ≤ `a`, `b` ≤ 1000
- `+` and `-` are not allowed

## Edge cases

- Negative operands (Python integers are unbounded, so masking to 32 bits matters)
- Zero
- Opposite signs

## Examples

| Input | Output | Why |
|---|---|---|
| `a = 4, b = 9` | `13` | positive |
| `a = -6, b = 2` | `-4` | mixed signs |
| `a = 0, b = 0` | `0` | zero |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Math
</details>
<!-- topics:end -->
