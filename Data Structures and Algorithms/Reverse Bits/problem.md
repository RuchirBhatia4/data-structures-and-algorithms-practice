<!-- meta:start -->
# 190. Reverse Bits

**LeetCode:** [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Treat the input as a 32-bit integer and reverse the order of its 32 bits (bit 0 becomes bit 31, and so on). Return the resulting integer.

## Input

- `n`: integer

## Output

- The integer whose 32-bit pattern is the reverse of `n`'s.

## Constraints

- 0 ≤ `n` ≤ 2³¹ − 2
- `n` is even (so the result fits in a signed 32-bit integer)
- Follow-up: how would you optimize if this is called many times?

## Edge cases

- 0
- Leading zeros become trailing zeros and vice versa
- Bits near both ends

## Examples

| Input | Output | Why |
|---|---|---|
| `2` | `1073741824` | bit 1 becomes bit 30 (2³⁰) |
| `0` | `0` | no bits set |
| `6` | `1610612736` | bits 1 and 2 become bits 30 and 29 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Divide and Conquer
</details>
<!-- topics:end -->
