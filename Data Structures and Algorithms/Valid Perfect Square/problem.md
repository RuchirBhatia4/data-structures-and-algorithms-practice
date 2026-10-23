<!-- meta:start -->
# 367. Valid Perfect Square

**LeetCode:** [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether a positive integer is the square of an integer, without using a built-in square-root function.

## Input

- `num`: positive integer

## Output

- `True` if `num` is a perfect square, otherwise `False`.

## Constraints

- 1 ≤ `num` ≤ 2³¹ − 1
- No library square root

## Edge cases

- 1
- Large values near 2³¹
- Numbers just above or below a square

## Examples

| Input | Output | Why |
|---|---|---|
| `49` | `True` | 7 × 7 |
| `50` | `False` | between 49 and 64 |
| `1` | `True` | 1 × 1 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Binary Search · Math
</details>
<!-- topics:end -->
