<!-- meta:start -->
# 338. Counting Bits

**LeetCode:** [338. Counting Bits](https://leetcode.com/problems/counting-bits/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

For every integer `i` from 0 to `n`, count the 1 bits in its binary representation, and return all the counts in a list.

## Input

- `n`: non-negative integer

## Output

- A list `ans` of length `n + 1` where `ans[i]` is the number of 1 bits in `i`.

## Constraints

- 0 ≤ `n` ≤ 10⁵
- Follow-up: linear time, ideally in one pass, without a built-in bit counter

## Edge cases

- `n = 0`
- Powers of two
- Large `n`

## Examples

| Input | Output | Why |
|---|---|---|
| `n = 0` | `[0]` | only 0 |
| `n = 4` | `[0, 1, 1, 2, 1]` | 0, 1, 10, 11, 100 |
| `n = 6` | `[0, 1, 1, 2, 1, 2, 2]` | … 101, 110 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Bit Manipulation · Dynamic Programming
</details>
<!-- topics:end -->
