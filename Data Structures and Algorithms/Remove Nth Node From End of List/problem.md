<!-- meta:start -->
# 19. Remove Nth Node From End of List

**LeetCode:** [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Remove the `n`-th node counted from the end of the list and return the head of the resulting list.

## Input

- `head`: first node of a linked list
- `n`: position from the end (1 = last node)

## Output

- The head of the list after the removal (possibly `None`).

## Constraints

- 1 to 30 nodes
- 0 ≤ `Node.val` ≤ 100
- 1 ≤ `n` ≤ number of nodes
- Follow-up: a single pass

## Edge cases

- Removing the head (`n` equals the length)
- Removing the only node
- Removing the last node

## Examples

| Input | Output | Why |
|---|---|---|
| `4 → 8 → 15 → 16 → 23, n = 2` | `4 → 8 → 15 → 23` | 16 is second from the end |
| `4, n = 1` | `empty list` | only node removed |
| `4 → 8, n = 2` | `8` | the head is removed |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Two Pointers
</details>
<!-- topics:end -->
