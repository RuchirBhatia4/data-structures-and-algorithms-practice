<!-- meta:start -->
# 252. Meeting Rooms

**LeetCode:** [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) · **Difficulty:** Easy · LeetCode Premium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Given meeting time intervals `[start, end]`, decide whether one person could attend all of them, meaning no two meetings overlap. A meeting that ends exactly when another starts is not an overlap.

## Input

- `intervals`: list of `[start, end]` pairs

## Output

- `True` if no meetings overlap, otherwise `False`.

## Constraints

- Up to about 10⁴ meetings
- `start < end`
- _Exact limits: see the official problem._

## Edge cases

- No meetings
- Meetings that touch at an endpoint
- Input not sorted by start time

## Examples

| Input | Output | Why |
|---|---|---|
| `[[0, 5], [5, 10]]` | `True` | touching is fine |
| `[[1, 4], [3, 6]]` | `False` | 3 is before 4 |
| `[]` | `True` | nothing to attend |

> NeetCode's version passes `Interval` objects with `start` and `end` attributes instead of pairs.

<!-- topics:start -->
<details>
<summary>Topics</summary>

Intervals · Array · Sorting · Quicksort
</details>
<!-- topics:end -->
