<!-- meta:start -->
# 1448. Count Good Nodes in Binary Tree

**LeetCode:** [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

A node is *good* if no node on the path from the root to it has a larger value. Count the good nodes.

## Input

- `root`: root of a non-empty binary tree

## Output

- The number of good nodes.

## Constraints

- 1 to 10⁵ nodes
- −10⁴ ≤ `Node.val` ≤ 10⁴

## Edge cases

- Equal values along a path (still good)
- Negative values
- Single node (the root is always good)

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 6, 2, 7, 1]` | `3` | 5, 6 and 7 are good; 2 and 1 are not |
| `[-1]` | `1` | the root |
| `[2, 2, 2]` | `3` | equal counts as good |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
