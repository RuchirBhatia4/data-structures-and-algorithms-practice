<!-- meta:start -->
# 875. Koko Eating Bananas

**LeetCode:** [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

There are piles of bananas and `h` hours. Pick an eating speed `k` (bananas per hour). Each hour you choose one pile and eat `k` bananas from it, or the whole pile if it has fewer, and you do not move to another pile within that hour. Return the smallest `k` that finishes every pile within `h` hours.

## Input

- `piles`: list of positive integers
- `h`: hours available

## Output

- The minimum integer eating speed.

## Constraints

- 1 ≤ `len(piles)` ≤ 10⁴
- `len(piles)` ≤ `h` ≤ 10⁹
- 1 ≤ `piles[i]` ≤ 10⁹

## Edge cases

- `h` equal to the number of piles (speed must be the largest pile)
- Very large `h` (speed 1)
- One huge pile
- Values that overflow in other languages

## Examples

| Input | Output | Why |
|---|---|---|
| `piles = [4, 9, 6], h = 6` | `4` | speed 4 needs 1 + 3 + 2 = 6 hours; speed 3 needs 7 |
| `piles = [10], h = 3` | `4` | speed 4 needs 3 hours; speed 3 needs 4 |
| `piles = [1, 1, 1], h = 3` | `1` | one hour per pile |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Binary Search · Array
</details>
<!-- topics:end -->
