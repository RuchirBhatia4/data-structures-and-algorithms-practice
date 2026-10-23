<!-- meta:start -->
# 904. Fruit Into Baskets

**LeetCode:** [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Trees stand in a row and `fruits[i]` is the type of fruit on tree `i`. You have two baskets, and each basket can hold any amount of a single fruit type. Starting at any tree and moving right, you pick exactly one fruit from every tree, and you must stop as soon as a fruit does not fit in either basket. Return the most fruit you can collect.

## Input

- `fruits`: list of integers (fruit types)

## Output

- The maximum number of fruits that can be picked.

## Constraints

- 1 ≤ `len(fruits)` ≤ 10⁵
- 0 ≤ `fruits[i]` < `len(fruits)`

## Edge cases

- Only one fruit type
- Exactly two types
- Best stretch starts in the middle
- Single tree

## Examples

| Input | Output | Why |
|---|---|---|
| `[0, 1, 0, 2, 2]` | `3` | trees 0–2 or trees 2–4 |
| `[3, 3, 3]` | `3` | one type fills one basket |
| `[1, 2, 3, 2, 2]` | `4` | trees 1–4 hold types 2 and 3 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sliding Window · Array · Hash Table
</details>
<!-- topics:end -->
