<!-- meta:start -->
# 146. LRU Cache

**LeetCode:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/) · **Difficulty:** Medium
<!-- meta:end -->

<!-- doc-status: written -->
## Problem

Design a fixed-capacity key–value cache that evicts the **least recently used** key when it is full. Both reading and writing a key count as using it. `get` and `put` must each run in O(1) average time.

## Input

- `LRUCache(capacity)` creates an empty cache
- `get(key)` returns the value for `key`, or −1 if absent
- `put(key, value)` inserts or updates; if this exceeds the capacity, evict the least recently used key

## Output

- `get` returns an integer; `put` returns nothing.

## Constraints

- 1 ≤ `capacity` ≤ 3000
- 0 ≤ `key` ≤ 10⁴
- 0 ≤ `value` ≤ 10⁵
- At most 2 × 10⁵ calls in total
- Required: O(1) average time per call

## Edge cases

- Updating an existing key (no eviction, but it becomes most recent)
- `get` refreshing a key's recency
- Capacity 1
- `get` on a key that was evicted

## Examples

| Input | Output | Why |
|---|---|---|
| `LRUCache(2)`, `put(1, 10)`, `put(2, 20)`, `get(1)` | `10` | key 1 is now most recent |
| then `put(3, 30)`, `get(2)` | `-1` | key 2 was least recent, so it was evicted |
| then `put(1, 15)`, `get(1)`, `get(3)` | `15`, `30` | update in place; 3 still cached |

<!-- topics:start -->
<details>
<summary>Topics</summary>

Linked List · Hash Table · Design · Doubly-Linked List
</details>
<!-- topics:end -->
