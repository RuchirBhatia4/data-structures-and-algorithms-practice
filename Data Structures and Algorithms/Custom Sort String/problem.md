<!-- meta:start -->
# 791. Custom Sort String

**LeetCode:** [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

`order` lists some distinct letters in a custom order. Rearrange the letters of `s` so that letters that appear in `order` follow that relative order. Letters of `s` that are not in `order` may go anywhere. Any valid rearrangement is accepted.

## Input

- `order`: string of distinct lowercase letters
- `s`: lowercase string to rearrange

## Output

- A permutation of `s` that respects the order given by `order`.

## Constraints

- 1 ≤ `len(order)` ≤ 26, all letters distinct
- 1 ≤ `len(s)` ≤ 200
- Lowercase English letters only

## Edge cases

- Letters in `s` that are missing from `order`
- Letters in `order` that are missing from `s`
- Repeated letters in `s`

## Examples

| Input | Output | Why |
|---|---|---|
| `order = "dcba", s = "abcd"` | `"dcba"` | every letter is ranked |
| `order = "xy", s = "yyx"` | `"xyy"` | x before both y |
| `order = "dcb", s = "abcd"` | any of `"adcb"`, `"dacb"`, `"dcab"`, `"dcba"` | `a` is unranked, so it may go anywhere |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Arrays & Hashing · Hash Table · String · Sorting
</details>
<!-- topics:end -->
