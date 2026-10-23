<!-- meta:start -->
# 112. Path Sum

**LeetCode:** [112. Path Sum](https://leetcode.com/problems/path-sum/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether the tree has a path from the root down to a **leaf** (a node with no children) whose values add up to `targetSum`.

## Input

- `root`: root of a binary tree (or `None`)
- `targetSum`: integer

## Output

- `True` if such a root-to-leaf path exists, otherwise `False`.

## Constraints

- 0 to 5000 nodes
- −1000 ≤ `Node.val` ≤ 1000
- −1000 ≤ `targetSum` ≤ 1000

## Edge cases

- Empty tree (always `False`)
- A prefix that matches but does not end at a leaf
- Negative values

## Examples

| Input | Output | Why |
|---|---|---|
| `root = [5, 3, 8, 2], targetSum = 10` | `True` | 5 → 3 → 2 |
| `root = [5, 3, 8, 2], targetSum = 13` | `True` | 5 → 8 |
| `root = [5, 3, 8, 2], targetSum = 8` | `False` | 5 + 3 = 8, but 3 is not a leaf |
| `root = [], targetSum = 0` | `False` | no paths |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Breadth-First Search · Binary Tree
</details>
<!-- topics:end -->
