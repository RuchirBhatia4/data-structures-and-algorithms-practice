<!-- meta:start -->
# 199. Binary Tree Right Side View

**LeetCode:** [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Imagine standing to the right of the tree. Return the value you would see on each level, from top to bottom: the right-most node of every level.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- A list with one value per level.

## Constraints

- 0 to 100 nodes
- −100 ≤ `Node.val` ≤ 100

## Edge cases

- A deeper level whose only node is on the left
- Empty tree
- Left-leaning chain

## Examples

| Input | Output | Why |
|---|---|---|
| `[6, 2, 9, 1]` | `[6, 9, 1]` | 1 is the only node on the third level |
| `[]` | `[]` | empty tree |
| `[3, 7, null, 5]` | `[3, 7, 5]` | everything is on the left |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
