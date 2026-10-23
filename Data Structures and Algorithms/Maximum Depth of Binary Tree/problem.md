<!-- meta:start -->
# 104. Maximum Depth of Binary Tree

**LeetCode:** [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the number of nodes on the longest path from the root down to a leaf.

## Input

- `root`: root of a binary tree (or `None`)

## Output

- The maximum depth (0 for an empty tree).

## Constraints

- 0 to 10⁴ nodes
- −100 ≤ `Node.val` ≤ 100

## Edge cases

- Empty tree
- A tree shaped like a linked list
- Deepest leaf on the right

## Examples

| Input | Output | Why |
|---|---|---|
| `[5, 3, 8, null, null, 7]` | `3` | 5 → 8 → 7 |
| `[]` | `0` | empty tree |
| `[1]` | `1` | just the root |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
