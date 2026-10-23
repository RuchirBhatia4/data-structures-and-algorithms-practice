<!-- meta:start -->
# 230. Kth Smallest Element in a BST

**LeetCode:** [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Return the `k`-th smallest value (counting from 1) stored in a binary search tree.

## Input

- `root`: root of a BST with `n` nodes
- `k`: rank to return

## Output

- The `k`-th smallest value.

## Constraints

- 1 ≤ `k` ≤ n ≤ 10⁴
- 0 ≤ `Node.val` ≤ 10⁴
- Follow-up: if the BST changes often and this query is frequent, how would you speed it up?

## Edge cases

- `k = 1` (minimum)
- `k = n` (maximum)
- Single node

## Examples

| Input | Output | Why |
|---|---|---|
| `root = [8, 4, 12, 2, 6], k = 3` | `6` | sorted values 2, 4, 6, 8, 12 |
| `root = [8, 4, 12, 2, 6], k = 5` | `12` | the largest |
| `root = [1], k = 1` | `1` | single node |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Search Tree · Binary Tree
</details>
<!-- topics:end -->
