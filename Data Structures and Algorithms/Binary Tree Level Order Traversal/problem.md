<!-- meta:start -->
# 102. Binary Tree Level Order Traversal

**LeetCode:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the node values level by level, from top to bottom, and left to right within each level.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- A list of levels, each a list of values.

## Constraints

- 0 to 2000 nodes
- −1000 ≤ `Node.val` ≤ 1000

## Edge cases

- Empty tree
- Missing children in the middle of a level
- Single node

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 8, null, 4]` | `[[5], [3, 8], [4]]` | 4 is the right child of 3 |
| `[]` | `[]` | empty tree |
| `[1]` | `[[1]]` | one level |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
