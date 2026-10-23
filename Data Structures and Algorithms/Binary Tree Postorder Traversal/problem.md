<!-- meta:start -->
# 145. Binary Tree Postorder Traversal

**LeetCode:** [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the node values in postorder: left subtree, then right subtree, then the node itself.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- A list of values in postorder.

## Constraints

- 0 to 100 nodes
- −100 ≤ `Node.val` ≤ 100
- Follow-up: the recursive version is easy; write it iteratively

## Edge cases

- Empty tree
- Only right children
- Single node

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 8, 1]` | `[1, 3, 8, 5]` | children before parents |
| `[]` | `[]` | empty tree |
| `[2, null, 7]` | `[7, 2]` | right child, then root |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Stack · Tree · Depth-First Search · Binary Tree
</details>
<!-- topics:end -->
