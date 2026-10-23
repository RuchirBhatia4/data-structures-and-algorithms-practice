<!-- meta:start -->
# 70. Climbing Stairs

**LeetCode:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A staircase has `n` steps. Each move climbs either 1 or 2 steps. Count the distinct sequences of moves that reach the top.

## Input

- `n`: number of steps

## Output

- The number of distinct ways to climb to the top.

## Constraints

- 1 ≤ `n` ≤ 45

## Edge cases

- `n = 1`
- `n = 2`
- Largest `n` (the answer is large but fits in 32 bits)

## Examples

| Input | Output | Why |
|---|---|---|
| `n = 1` | `1` | one single step |
| `n = 4` | `5` | 1111, 112, 121, 211, 22 |
| `n = 5` | `8` | ways(4) + ways(3) |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Dynamic Programming · Math · Memoization
</details>
<!-- topics:end -->
