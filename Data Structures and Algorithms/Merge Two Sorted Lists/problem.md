<!-- meta:start -->
# 21. Merge Two Sorted Lists

**LeetCode:** [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Two linked lists are each sorted in non-decreasing order. Combine them into one sorted list by relinking their existing nodes, and return its head.

## Input

- `list1`, `list2`: heads of sorted linked lists (either may be empty)

## Output

- The head of the merged sorted list.

## Constraints

- 0 to 50 nodes in each list
- −100 ≤ `Node.val` ≤ 100
- Both inputs are sorted in non-decreasing order

## Edge cases

- One or both lists empty
- Equal values in both lists
- All of one list smaller than the other

## Examples

| Input | Output | Why |
|---|---|---|
| `1 → 4 → 5 and 2 → 4` | `1 → 2 → 4 → 4 → 5` | interleaved |
| `empty and 0` | `0` | one list empty |
| `empty and empty` | `empty list` | nothing to merge |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Recursion
</details>
<!-- topics:end -->
