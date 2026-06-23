# 206. Reverse Linked List

## Problem

Given the head of a singly linked list, reverse the list and return the new head.

---

## Key Idea

We reverse the list by changing the direction of the `.next` pointers.

### Example

**Before:**
```
1 → 2 → 3 → None
```

**After:**
```
1 ← 2 ← 3
```

We do NOT create new nodes — we only rewire existing pointers.

---

## Approach

We use three pointers:

- `prev` → reversed portion of the list
- `curr` → current node
- `next_node` → stores the next node so we don’t lose the rest of the list

---

## Algorithm

For each node:

1. Save the next node
2. Reverse the current pointer
3. Move `prev` forward
4. Move `curr` forward

---

## Solution

```python
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next node
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev
```

---

## Dry Run

Input:
```
1 → 2 → 3 → None
```

### Step-by-step:

- Start:
  ```
  prev = None
  curr = 1
  ```

- Step 1:
  ```
  1 → None
  prev = 1
  curr = 2
  ```

- Step 2:
  ```
  2 → 1 → None
  prev = 2
  curr = 3
  ```

- Step 3:
  ```
  3 → 2 → 1 → None
  prev = 3
  curr = None
  ```

Final head = `prev`

---

## Complexity Analysis

### Time Complexity
```
O(n)
```
We visit each node once.

### Space Complexity
```
O(1)
```
We only use pointers, no extra data structures.

---

## Key Takeaways

- Linked lists cannot be iterated like Python lists
- Always use `.next` to traverse
- Reversal is done by changing pointers, not values
- Always store `next_node` before breaking links