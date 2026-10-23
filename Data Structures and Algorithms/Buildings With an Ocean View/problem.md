<!-- meta:start -->
# 1762. Buildings With an Ocean View

**LeetCode:** [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) · **Difficulty:** Medium · LeetCode Premium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Buildings stand in a line with the ocean to the right. A building has an ocean view if every building to its right is strictly shorter. Return the indices of all buildings with an ocean view in increasing order.

## Input

- `heights`: list of positive integers

## Output

- A sorted list of indices of buildings that can see the ocean.

## Constraints

- Up to about 10⁵ buildings
- Positive heights
- _Exact limits: see the official problem._

## Edge cases

- Equal heights (the left one is blocked)
- Strictly increasing heights (only the last one)
- Strictly decreasing heights (all of them)

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 4, 1]` | `[0, 2, 3]` | 3 is blocked by 4 |
| `[2, 2, 2]` | `[2]` | equal heights block |
| `[1, 2, 3]` | `[2]` | only the last building |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · Array · Monotonic Stack
</details>
<!-- topics:end -->
