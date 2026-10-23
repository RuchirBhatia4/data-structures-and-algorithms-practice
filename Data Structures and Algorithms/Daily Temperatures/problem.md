<!-- meta:start -->
# 739. Daily Temperatures

**LeetCode:** [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

For each day's temperature, find how many days you must wait until a **strictly** warmer day. Use 0 when no warmer day follows.

## Input

- `temperatures`: list of integers

## Output

- A list of the same length with the waiting time for each day.

## Constraints

- 1 ≤ `len(temperatures)` ≤ 10⁵
- 30 ≤ `temperatures[i]` ≤ 100

## Edge cases

- Equal temperatures (not warmer)
- Strictly decreasing temperatures
- Last day is always 0

## Examples

| Input | Output | Why |
|---|---|---|
| `[50, 40, 45, 60]` | `[3, 1, 1, 0]` | each day's next warmer day |
| `[70, 70]` | `[0, 0]` | equal is not warmer |
| `[30, 31, 32]` | `[1, 1, 0]` | always warmer the next day |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · Array · Monotonic Stack
</details>
<!-- topics:end -->
