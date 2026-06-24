# 21. Merge Two Sorted Lists

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the merged list.

---

## Key Idea

Since both lists are already sorted, we can compare the current node of each list and always take the smaller value.

To simplify handling the head of the merged list, we use a **dummy node**.

---

## Approach

We use two pointers:

- `list1` → current node in the first list
- `list2` → current node in the second list

And two helper pointers:

- `dummy` → placeholder node before the merged list
- `current` → tracks the end of the merged list

---

## Algorithm

While both lists contain nodes:

1. Compare `list1.val` and `list2.val`
2. Attach the smaller node to the merged list
3. Move that list's pointer forward
4. Move `current` forward

After the loop:

- One list may still contain nodes
- Attach the remaining nodes directly

Finally:

- Return `dummy.next` because `dummy` is only a placeholder

---

## Code

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
```

---

## Dry Run

Input:

```
list1 = 1 → 2 → 4
list2 = 1 → 3 → 4
```

### Step 1

Compare:

```
1 and 1
```

Take first `1`

```
dummy → 1
```

### Step 2

Compare:

```
2 and 1
```

Take second `1`

```
dummy → 1 → 1
```

### Step 3

Compare:

```
2 and 3
```

Take `2`

```
dummy → 1 → 1 → 2
```

### Step 4

Compare:

```
4 and 3
```

Take `3`

```
dummy → 1 → 1 → 2 → 3
```

### Step 5

Compare:

```
4 and 4
```

Take first `4`

```
dummy → 1 → 1 → 2 → 3 → 4
```

The first list is exhausted.

Attach the remaining node:

```
dummy → 1 → 1 → 2 → 3 → 4 → 4
```

Return:

```
dummy.next
```

---

## Complexity Analysis

### Time Complexity

```
O(n + m)
```

Where:

- `n` = length of `list1`
- `m` = length of `list2`

Each node is visited exactly once.

### Space Complexity

```
O(1)
```

Only a few pointers are used.

---

## Key Takeaways

- Dummy nodes simplify linked list construction.
- Always move the pointer of the node you attach.
- Once one list is exhausted, the remaining nodes are already sorted.
- This is the same merge step used in Merge Sort.
- A common linked list pattern is:
  - Compare nodes
  - Attach the smaller node
  - Advance pointers
  - Attach leftovers