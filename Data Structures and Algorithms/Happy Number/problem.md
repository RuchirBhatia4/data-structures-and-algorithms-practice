<!-- meta:start -->
# 202. Happy Number

**LeetCode:** [202. Happy Number](https://leetcode.com/problems/happy-number/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Start with a positive integer and repeatedly replace it with the sum of the squares of its digits. The number is *happy* if this process reaches 1; otherwise it loops forever without reaching 1. Decide whether `n` is happy.

## Input

- `n`: positive integer

## Output

- `True` if `n` is happy, otherwise `False`.

## Constraints

- 1 ≤ `n` ≤ 2³¹ − 1

## Edge cases

- 1 itself
- A number that falls into a loop
- Large inputs (the sequence shrinks quickly)

## Examples

| Input | Output | Why |
|---|---|---|
| `7` | `True` | 7 → 49 → 97 → 130 → 10 → 1 |
| `4` | `False` | 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 |
| `1` | `True` | already 1 |

> NeetCode calls this problem *Non-Cyclical Number*.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Math & Geometry · Hash Table · Math · Two Pointers · Floyd's Cycle Finding Algorithm
</details>
<!-- topics:end -->
