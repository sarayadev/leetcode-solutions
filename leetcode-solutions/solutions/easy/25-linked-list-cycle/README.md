# 141. Linked List Cycle

## Problem

Given the head of a linked list, determine if the linked list contains a cycle.

A cycle exists if a node can be reached again by continuously following the `next` pointer.

Return `True` if there is a cycle, otherwise return `False`.

---

## Key Idea

Use two pointers moving at different speeds:

- `slow` moves one step at a time
- `fast` moves two steps at a time

If a cycle exists, the fast pointer will eventually catch the slow pointer.

This technique is called **Floyd's Cycle Detection Algorithm (Tortoise and Hare)**.

---

## Approach

Initialize:

- `slow = head`
- `fast = head`

While `fast` and `fast.next` exist:

1. Move `slow` one step
2. Move `fast` two steps
3. If they meet, a cycle exists

If the loop ends, there is no cycle.

---

## Algorithm

1. Set `slow` and `fast` to the head
2. Move pointers until the fast pointer reaches the end
3. If `slow == fast` at any point, return `True`
4. Return `False`

---

## Code

```python
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

---

## Dry Run

Input:

```
3 → 2 → 0 → -4
    ↑       ↓
    ← ← ← ←
```

### Step 1

```
slow = 2
fast = 0
```

### Step 2

```
slow = 0
fast = 2
```

### Step 3

```
slow = -4
fast = -4
```

Pointers meet.

Return:

```
True
```

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

### Space Complexity

```
O(1)
```

---

## Key Takeaways

- Floyd's Algorithm detects cycles efficiently.
- Fast moves twice as quickly as slow.
- If a cycle exists, they must eventually meet.
- No extra memory is required.

---