<!-- meta:start -->
# 110. Balanced Binary Tree

**LeetCode:** [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A tree is height-balanced when, at **every** node, the heights of the left and right subtrees differ by at most one. Decide whether the tree is height-balanced.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- `True` if the tree is height-balanced, otherwise `False`.

## Constraints

- 0 to 5000 nodes
- −10⁴ ≤ `Node.val` ≤ 10⁴

## Edge cases

- Empty tree (balanced)
- Balanced at the root but not deeper down
- A single long chain

## Examples

| Input | Output | Why |
|---|---|---|
| `[4, 2, 6, 1]` | `True` | subtree heights 2 and 1 |
| `[4, 2, null, 1]` | `False` | heights 2 and 0 at the root |
| `[]` | `True` | empty tree |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Tree
</details>
<!-- topics:end -->
