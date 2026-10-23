<!-- meta:start -->
# Quick Sort

**Source:** NeetCode course exercise (not on LeetCode)
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Sort a list of key–value pairs by key in place using quicksort, and return the list. This version is not required to keep equal keys in their original order.

## Input

- `pairs`: list of `Pair` objects with an integer `key` and a string `value`

## Output

- The pairs sorted by key.

## Constraints

- Limits come from NeetCode's exercise and were not checked

## Edge cases

- Empty list
- Already sorted input (worst case for a last-element pivot)
- Many equal keys

## Examples

| Input | Output | Why |
|---|---|---|
| `[(3, "c"), (1, "a"), (2, "b")]` | `[(1, "a"), (2, "b"), (3, "c")]` | by key |
| `[]` | `[]` | empty |
| `[(2, "x"), (2, "y")]` | keys `[2, 2]`, values in either order | not necessarily stable |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sorting
</details>
<!-- topics:end -->
