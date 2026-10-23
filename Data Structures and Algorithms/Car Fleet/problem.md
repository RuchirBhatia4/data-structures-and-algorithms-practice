<!-- meta:start -->
# 853. Car Fleet

**LeetCode:** [853. Car Fleet](https://leetcode.com/problems/car-fleet/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Cars drive toward `target` on a single-lane road. Car `i` starts at `position[i]` with speed `speed[i]`. A car can never pass the one ahead of it: if it catches up, the two drive together at the slower speed and count as one fleet (catching up exactly at the target also counts). Return how many fleets arrive at the target.

## Input

- `target`: destination position
- `position`: distinct starting positions
- `speed`: speed of each car

## Output

- The number of car fleets that reach the target.

## Constraints

- 1 ≤ n ≤ 10⁵ cars
- 0 < `target` ≤ 10⁶
- 0 ≤ `position[i]` < `target`, all distinct
- 0 < `speed[i]` ≤ 10⁶

## Edge cases

- A single car
- Catching up exactly at the target
- A fast car behind a slow car that is itself behind a faster car
- Input positions not sorted

## Examples

| Input | Output | Why |
|---|---|---|
| `target = 12, position = [8, 0, 4], speed = [1, 2, 2]` | `2` | cars at 8 and 4 both need 4 hours; the car at 0 needs 6 |
| `target = 10, position = [0, 5], speed = [1, 1]` | `2` | equal speeds never meet |
| `target = 10, position = [6, 0], speed = [1, 5]` | `1` | the fast car catches the slow one at 7.5 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Stack · Array · Sorting · Monotonic Stack
</details>
<!-- topics:end -->
