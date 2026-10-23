<!-- meta:start -->
# 1046. Last Stone Weight

**LeetCode:** [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Repeatedly take the two heaviest stones and smash them together. If they weigh the same, both are destroyed; otherwise the lighter one is destroyed and the heavier one loses that much weight. Return the weight of the last remaining stone, or 0 if none remain.

## Input

- `stones`: list of positive integer weights

## Output

- The weight of the final stone, or 0.

## Constraints

- 1 ≤ `len(stones)` ≤ 30
- 1 ≤ `stones[i]` ≤ 1000

## Edge cases

- Single stone
- Two equal stones
- Everything cancels out

## Examples

| Input | Output | Why |
|---|---|---|
| `[3, 7, 2]` | `2` | 7 vs 3 leaves 4; 4 vs 2 leaves 2 |
| `[5, 5]` | `0` | both destroyed |
| `[9]` | `9` | nothing to smash |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Heap / Priority Queue · Array · Heap (Priority Queue)
</details>
<!-- topics:end -->
