<!-- meta:start -->
# 746. Min Cost Climbing Stairs

**LeetCode:** [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

`cost[i]` is what you pay when you step on stair `i`; after paying you may climb one or two stairs. You can start on stair 0 or stair 1, and the top is just past the last stair. Return the cheapest total cost to reach the top.

## Input

- `cost`: list of non-negative integers

## Output

- The minimum total cost.

## Constraints

- 2 ≤ `len(cost)` ≤ 1000
- 0 ≤ `cost[i]` ≤ 999

## Edge cases

- Only two stairs
- All costs zero
- Skipping an expensive stair

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 1, 4]` | `1` | start on stair 1, pay 1, jump two to the top |
| `[0, 0]` | `0` | free stairs |
| `[7, 2, 2, 8]` | `4` | stairs 1 and 2, then two steps to the top |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Dynamic Programming · Array
</details>
<!-- topics:end -->
