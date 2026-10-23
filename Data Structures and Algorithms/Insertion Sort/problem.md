<!-- meta:start -->
# Insertion Sort

**Source:** NeetCode course exercise (not on LeetCode)
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Sort a list of key–value pairs by key using insertion sort, keeping pairs with equal keys in their original order. Return a snapshot of the whole list after each element has been inserted into the sorted prefix (one snapshot per element).

## Input

- `pairs`: list of `Pair` objects with an integer `key` and a string `value`

## Output

- A list of snapshots; the last snapshot is the fully sorted list.

## Constraints

- Limits come from NeetCode's exercise and were not checked

## Edge cases

- Empty list (no snapshots)
- Equal keys must keep their order
- Already sorted input

## Examples

| Input | Output | Why |
|---|---|---|
| `[(5, "x"), (2, "y")]` | `[[(5, "x"), (2, "y")], [(2, "y"), (5, "x")]]` | one snapshot per element |
| `[(1, "a"), (1, "b")]` | `[[(1, "a"), (1, "b")], [(1, "a"), (1, "b")]]` | equal keys stay in order |

> Pairs are written as `(key, value)`.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Sorting
</details>
<!-- topics:end -->
