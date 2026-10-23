<!-- meta:start -->
# 141. Linked List Cycle

**LeetCode:** [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether a linked list contains a cycle, meaning that following `next` pointers eventually revisits a node.

## Input

- `head`: first node of a singly linked list (or `None`)

## Output

- `True` if there is a cycle, otherwise `False`.

## Constraints

- 0 to 10⁴ nodes
- −10⁵ ≤ `Node.val` ≤ 10⁵
- Follow-up: O(1) extra memory

## Edge cases

- Empty list
- Single node pointing to itself
- Cycle back to the head
- Long list with no cycle

## Examples

| Input | Output | Why |
|---|---|---|
| 3 → 8 → 1 → 6, with 6 linking back to 8 | `True` | the walk repeats 8 → 1 → 6 |
| 1 → 2 → end | `False` | reaches the end |
| one node linking to itself | `True` | smallest cycle |
| empty list | `False` | no nodes |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Hash Table · Two Pointers · Floyd's Cycle Finding Algorithm
</details>
<!-- topics:end -->
