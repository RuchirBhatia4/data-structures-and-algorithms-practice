<!-- meta:start -->
# 143. Reorder List

**LeetCode:** [143. Reorder List](https://leetcode.com/problems/reorder-list/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Rearrange a list `L0 → L1 → … → Ln` **in place** into `L0 → Ln → L1 → Ln−1 → L2 → …`, alternating between the front and the back. Only links may change, not node values.

## Input

- `head`: first node of a non-empty linked list (modified in place)

## Output

- Nothing is returned; the list is relinked.

## Constraints

- 1 to 5 × 10⁴ nodes
- 1 ≤ `Node.val` ≤ 1000

## Edge cases

- One node
- Two nodes (unchanged)
- Odd and even lengths

## Examples

| Input | Output | Why |
|---|---|---|
| `10 → 20 → 30 → 40 → 50 → 60` | `10 → 60 → 20 → 50 → 30 → 40` | front, back, front, back… |
| `3 → 6 → 9` | `3 → 9 → 6` | odd length |
| `7` | `7` | single node |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Two Pointers · Stack · Recursion
</details>
<!-- topics:end -->
