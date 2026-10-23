<!-- meta:start -->
# 100. Same Tree

**LeetCode:** [100. Same Tree](https://leetcode.com/problems/same-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether two binary trees are identical: the same shape, with equal values in corresponding nodes.

## Input

- `p`, `q`: roots of two binary trees (either may be `None`)

## Output

- `True` if the trees are identical, otherwise `False`.

## Constraints

- 0 to 100 nodes in each tree
- −10⁴ ≤ `Node.val` ≤ 10⁴

## Edge cases

- Both empty
- Same values, different shape
- One empty, one not

## Examples

| Input | Output | Why |
|---|---|---|
| `p = [1, 2], q = [1, 2]` | `True` | same shape and values |
| `p = [1, 2], q = [1, null, 2]` | `False` | 2 is a left child vs. a right child |
| `p = [], q = []` | `True` | both empty |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
