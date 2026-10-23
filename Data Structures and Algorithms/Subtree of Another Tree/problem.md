<!-- meta:start -->
# 572. Subtree of Another Tree

**LeetCode:** [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) · **Difficulty:** Easy
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Decide whether `subRoot` appears inside `root` as a complete subtree: some node of `root` together with **all** of its descendants must be identical to `subRoot`.

## Input

- `root`: root of the larger tree
- `subRoot`: root of the tree to look for

## Output

- `True` if such a node exists, otherwise `False`.

## Constraints

- 1 to 2000 nodes in `root`
- 1 to 1000 nodes in `subRoot`
- −10⁴ ≤ values ≤ 10⁴

## Edge cases

- A match except for extra descendants (not a subtree)
- `subRoot` equal to the whole tree
- Repeated values

## Examples

| Input | Output | Why |
|---|---|---|
| `root = [5, 3, 8, 1, 4], subRoot = [3, 1, 4]` | `True` | the left subtree matches |
| `root = [5, 3, 8, 1, 4, null, null, null, null, 2], subRoot = [3, 1, 4]` | `False` | 4 has an extra child in `root` |
| `root = [2], subRoot = [2]` | `True` | the whole tree |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · String Matching · Binary Tree · Hash Function
</details>
<!-- topics:end -->
