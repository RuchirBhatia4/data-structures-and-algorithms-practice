<!-- meta:start -->
# 2. Add Two Numbers

**LeetCode:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Two non-empty linked lists each represent a non-negative integer with its digits stored in **reverse** order (ones digit first). Return their sum as a linked list in the same reverse-digit format.

## Input

- `l1`, `l2`: heads of linked lists of digits

## Output

- The head of a linked list holding the sum's digits, ones digit first.

## Constraints

- 1 to 100 nodes per list
- 0 ≤ `Node.val` ≤ 9
- No leading zeros except the number 0 itself

## Edge cases

- Different lengths
- A final carry that adds a new digit
- Both numbers zero

## Examples

| Input | Output | Why |
|---|---|---|
| `4 → 1 and 7 → 9` | `1 → 1 → 1` | 14 + 97 = 111 |
| `0 and 0` | `0` | zero |
| `9 → 9 and 1` | `0 → 0 → 1` | 99 + 1 = 100 |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Math · Recursion
</details>
<!-- topics:end -->
