<!-- meta:start -->
# Singly Linked List

**Source:** NeetCode course exercise (not on LeetCode)
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Implement a singly linked list class with zero-based indexing that supports reading by index, inserting at either end, removing by index, and listing its values.

## Input

- `LinkedList()` creates an empty list
- `get(index)` returns the value at `index`, or −1 if out of range
- `insertHead(val)` and `insertTail(val)` add a value at the front or back
- `remove(index)` removes the node at `index` and returns `True`, or returns `False` if out of range
- `getValues()` returns all values from head to tail

## Output

- `get` returns an integer, `remove` a boolean, `getValues` a list; inserts return nothing.

## Constraints

- Exact limits come from NeetCode's exercise and were not checked

## Edge cases

- Operations on an empty list
- Removing the head and the tail
- Inserting at the tail after removing the tail
- Negative or too-large indices

## Examples

| Input | Output | Why |
|---|---|---|
| `insertTail(1)`, `insertHead(0)`, `insertTail(2)`, `getValues()` | `[0, 1, 2]` | both ends used |
| then `get(1)`, `remove(5)` | `1`, `False` | index 5 does not exist |
| then `remove(0)`, `getValues()`, `get(2)` | `True`, `[1, 2]`, `-1` | head removed; index 2 now out of range |

> NeetCode foundations exercise ("Design Singly Linked List"). LeetCode 707 *Design Linked List* is similar but has a different interface.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List
</details>
<!-- topics:end -->
