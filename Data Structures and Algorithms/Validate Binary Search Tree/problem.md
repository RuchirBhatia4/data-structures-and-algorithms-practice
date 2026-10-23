<!-- meta:start -->
# 98. Validate Binary Search Tree

**LeetCode:** [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether a binary tree is a valid binary search tree: for every node, all values in its left subtree are strictly smaller and all values in its right subtree are strictly larger, and both subtrees are valid too.

## Input

- `root`: root of a non-empty binary tree

## Output

- `True` if the tree is a valid BST, otherwise `False`.

## Constraints

- 1 to 10⁴ nodes
- −2³¹ ≤ `Node.val` ≤ 2³¹ − 1

## Edge cases

- A value that is fine for its parent but violates an ancestor
- Duplicate values (invalid)
- Values at the 32-bit limits

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 8]` | `True` | 3 < 5 < 8 |
| `[5, 3, 8, 1, 6]` | `False` | 6 is in 5's left subtree |
| `[2, 2]` | `False` | duplicates are not allowed |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Search Tree · Binary Tree
</details>
<!-- topics:end -->
