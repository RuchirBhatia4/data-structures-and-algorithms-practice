<!-- meta:start -->
# 235. Lowest Common Ancestor of a Binary Search Tree

**LeetCode:** [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

In a binary search tree, find the lowest common ancestor of nodes `p` and `q`: the deepest node that has both as descendants, where a node counts as a descendant of itself.

## Input

- `root`: root of a BST with distinct values
- `p`, `q`: two different nodes that exist in the tree

## Output

- The lowest common ancestor node.

## Constraints

- 2 to 10⁵ nodes
- −10⁹ ≤ `Node.val` ≤ 10⁹
- All values distinct
- `p != q`, and both are in the tree

## Edge cases

- One node is the ancestor of the other
- Nodes in different subtrees of the root
- `p` greater than `q`

## Examples

| Input | Output | Why |
|---|---|---|
| `root = [8, 4, 12, 2, 6, 10, 14], p = 2, q = 6` | `4` | both are under 4 |
| `root = [8, 4, 12, 2, 6, 10, 14], p = 6, q = 10` | `8` | they split at the root |
| `root = [8, 4, 12, 2, 6, 10, 14], p = 4, q = 6` | `4` | 4 is an ancestor of 6 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Search Tree · Binary Tree · Binary Lifting · Lowest Common Ancestor
</details>
<!-- topics:end -->
