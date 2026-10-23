<!-- meta:start -->
# 67. Add Binary

**LeetCode:** [67. Add Binary](https://leetcode.com/problems/add-binary/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Add two binary numbers given as strings and return their sum as a binary string.

## Input

- `a`, `b`: strings of `0`s and `1`s

## Output

- The binary string of `a + b`.

## Constraints

- 1 ≤ `len(a)`, `len(b)` ≤ 10⁴
- Only `0` and `1` characters
- No leading zeros except for `"0"` itself

## Edge cases

- Different lengths
- A final carry that adds a digit
- Both zero

## Examples

| Input | Output | Why |
|---|---|---|
| `a = "101", b = "11"` | `"1000"` | 5 + 3 = 8 |
| `a = "0", b = "0"` | `"0"` | zero |
| `a = "110", b = "1"` | `"111"` | 6 + 1 = 7 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Math · String · Simulation
</details>
<!-- topics:end -->
