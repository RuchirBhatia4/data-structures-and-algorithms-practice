<!-- meta:start -->
# 155. Min Stack

**LeetCode:** [155. Min Stack](https://leetcode.com/problems/min-stack/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Design a stack that, in addition to the usual operations, can report its smallest element. Every operation must take constant time.

## Input

- `MinStack()` creates an empty stack
- `push(value)` adds a value on top
- `pop()` removes the top value
- `top()` returns the top value
- `getMin()` returns the smallest value currently in the stack

## Output

- `top()` and `getMin()` return integers; the other operations return nothing.

## Constraints

- −2³¹ ≤ `value` ≤ 2³¹ − 1
- `pop`, `top` and `getMin` are only called on a non-empty stack
- At most 3 × 10⁴ calls in total
- Required: O(1) per operation

## Edge cases

- The minimum value pushed twice, then popped once
- Negative values
- Minimum removed, so it must revert
- Single element

## Examples

| Input | Output | Why |
|---|---|---|
| `push(5)`, `push(2)`, `push(8)`, `getMin()` | `2` | smallest of 5, 2, 8 |
| then `pop()`, `getMin()` | `2` | 8 removed |
| then `pop()`, `getMin()`, `top()` | `5`, `5` | 2 removed; only 5 left |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · Design
</details>
<!-- topics:end -->
