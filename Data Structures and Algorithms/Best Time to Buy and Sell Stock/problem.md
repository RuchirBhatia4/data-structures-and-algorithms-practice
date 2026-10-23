<!-- meta:start -->
# 121. Best Time to Buy and Sell Stock

**LeetCode:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

`prices[i]` is a stock's price on day `i`. Choose one day to buy and a **later** day to sell to make the largest possible profit. If no trade makes money, the answer is 0.

## Input

- `prices`: list of non-negative integers, one per day

## Output

- The maximum profit from a single buy followed by a single sell, or 0.

## Constraints

- 1 ≤ `len(prices)` ≤ 10⁵
- 0 ≤ `prices[i]` ≤ 10⁴

## Edge cases

- Prices only fall (answer 0)
- A single day
- Equal prices
- Lowest price comes after the highest price

## Examples

| Input | Output | Why |
|---|---|---|
| `[8, 3, 6, 1, 4]` | `3` | buy at 3 and sell at 6 (or buy at 1 and sell at 4) |
| `[9, 7, 4]` | `0` | no profitable trade |
| `[2, 2, 5]` | `3` | buy at 2, sell at 5 |
| `[5]` | `0` | cannot sell on a later day |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sliding Window · Array · Dynamic Programming
</details>
<!-- topics:end -->
