<!-- meta:start -->
# 543. Diameter of Binary Tree

**LeetCode:** [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

The diameter is the number of **edges** on the longest path between any two nodes. The path does not have to pass through the root. Return the diameter.

## Input

- `root`: root of a non-empty binary tree

## Output

- The length (in edges) of the longest path.

## Constraints

- 1 to 10⁴ nodes
- −100 ≤ `Node.val` ≤ 100

## Edge cases

- Single node (diameter 0)
- Longest path entirely inside one subtree
- A path that turns at the root

## Examples

| Input | Output | Why |
|---|---|---|
| `[7, 4, 9, 2, 5]` | `3` | 2 → 4 → 7 → 9 |
| `[1]` | `0` | no edges |
| `[1, 2, null, 3, 4, 5, null, null, 6]` | `4` | 5 → 3 → 2 → 4 → 6, which skips the root |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Tree · DP on Trees
</details>
<!-- topics:end -->
