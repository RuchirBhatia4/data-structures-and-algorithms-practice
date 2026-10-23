<!-- meta:start -->
# 105. Construct Binary Tree from Preorder and Inorder Traversal

**LeetCode:** [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given the preorder and inorder traversals of a binary tree with distinct values, rebuild the tree and return its root.

## Input

- `preorder`: values in root–left–right order
- `inorder`: values in left–root–right order

## Output

- The root of the reconstructed tree.

## Constraints

- 1 ≤ length ≤ 3000
- Both lists have the same length
- −3000 ≤ values ≤ 3000
- All values are distinct
- The lists are guaranteed to describe the same tree

## Edge cases

- Single node
- Every node has only a left child
- Every node has only a right child

## Examples

| Input | Output | Why |
|---|---|---|
| `preorder = [4, 2, 1, 3, 6], inorder = [1, 2, 3, 4, 6]` | `[4, 2, 6, 1, 3]` | 4 is the root; 1, 2, 3 are on its left |
| `preorder = [1, 2], inorder = [2, 1]` | `[1, 2]` | 2 is a left child |
| `preorder = [7], inorder = [7]` | `[7]` | single node |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Array · Hash Table · Divide and Conquer · Tree · Binary Tree
</details>
<!-- topics:end -->
