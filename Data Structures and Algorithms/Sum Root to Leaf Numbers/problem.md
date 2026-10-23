<!-- meta:start -->
# 129. Sum Root to Leaf Numbers

**LeetCode:** [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Every node holds a digit. Each root-to-leaf path spells a number (for example 1 → 2 → 3 is 123). Return the sum of the numbers for all root-to-leaf paths.

## Input

- `root`: root of a non-empty binary tree of digits

## Output

- The total of all root-to-leaf numbers.

## Constraints

- 1 to 1000 nodes
- 0 ≤ `Node.val` ≤ 9
- Depth at most 10
- The answer fits in a 32-bit integer

## Edge cases

- Single node
- Zeros inside a path
- Nodes with one child (only leaves end a number)

## Examples

| Input | Output | Why |
|---|---|---|
| `[4, 9, 0]` | `89` | 49 + 40 |
| `[2, 0, null, 5]` | `205` | a single path 2 → 0 → 5 |
| `[7]` | `7` | single node |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Trees · Tree · Depth-First Search · Binary Tree
</details>
<!-- topics:end -->
