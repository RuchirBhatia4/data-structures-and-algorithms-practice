<!-- meta:start -->
# Merge Sort

**Source:** NeetCode course exercise (not on LeetCode)
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Sort a list of key–value pairs by key using merge sort. Pairs with equal keys keep their original relative order.

## Input

- `pairs`: list of `Pair` objects with an integer `key` and a string `value`

## Output

- The pairs sorted by key.

## Constraints

- Limits come from NeetCode's exercise and were not checked

## Edge cases

- Empty list
- Equal keys (stability)
- Odd lengths when splitting

## Examples

| Input | Output | Why |
|---|---|---|
| `[(5, "apple"), (2, "banana"), (9, "cherry")]` | `[(2, "banana"), (5, "apple"), (9, "cherry")]` | by key |
| `[(3, "a"), (1, "b"), (3, "c")]` | `[(1, "b"), (3, "a"), (3, "c")]` | equal keys keep their order |
| `[]` | `[]` | empty |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sorting
</details>
<!-- topics:end -->
