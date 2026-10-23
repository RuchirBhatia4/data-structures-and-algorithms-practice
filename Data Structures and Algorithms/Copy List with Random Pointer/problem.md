<!-- meta:start -->
# 138. Copy List with Random Pointer

**LeetCode:** [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Every node has a `next` pointer and a `random` pointer that may point to any node in the list or to `None`. Build a deep copy: new nodes with the same values whose `next` and `random` pointers mirror the original structure. No pointer in the copy may refer to a node of the original list.

## Input

- `head`: first node of the list (or `None`); each node has `val`, `next` and `random`

## Output

- The head of the deep copy.

## Constraints

- 0 to 1000 nodes
- −10⁴ ≤ `Node.val` ≤ 10⁴
- `random` is `None` or points to a node in the same list

## Edge cases

- Empty list
- A node whose `random` points to itself
- Several nodes pointing to the same node
- Duplicate values (copy by identity, not by value)

## Examples

| Input | Output | Why |
|---|---|---|
| values 1, 2, 3 with random links none, node 1, node 3 | a new list with the same values and links | structure preserved |
| a single node 4 whose random points to itself | a new node 4 pointing to itself | self-reference copied |
| empty list | `None` | nothing to copy |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Hash Table
</details>
<!-- topics:end -->
