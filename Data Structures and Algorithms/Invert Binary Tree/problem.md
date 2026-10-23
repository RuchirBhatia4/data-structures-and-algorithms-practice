<!-- meta:start -->
# 226. Invert Binary Tree

**LeetCode:** [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Mirror a binary tree: swap the left and right children of every node. Return the root.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- The root of the mirrored tree.

## Constraints

- 0 to 100 nodes
- −100 ≤ `Node.val` ≤ 100

## Edge cases

- Empty tree
- Single node
- Nodes with only one child

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 8, 1, 4]` | `[5, 8, 3, null, null, 4, 1]` | every pair of children swapped |
| `[]` | `[]` | empty tree |
| `[2, 1]` | `[2, null, 1]` | the left child moves to the right |

> Trees are written in level order with `null` for missing children, as on LeetCode.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
