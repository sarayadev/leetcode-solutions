# 102. Binary Tree Level Order Traversal

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values.

Return values level by level from left to right.

---

## Key Idea

Use **Breadth-First Search (BFS)**.

A queue allows us to process nodes one level at a time.

---

## Approach

1. Put the root in a queue
2. Process all nodes currently in the queue
3. Store their values in a level list
4. Add their children to the queue
5. Repeat until the queue is empty

---

## Algorithm

1. Handle empty tree
2. Create queue containing root
3. While queue is not empty:
   - Process one level
   - Store values
   - Add children
4. Return all levels

---

## Code

```python
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
```

---

## Dry Run

Tree:

```
      3
     / \
    9  20
       / \
      15  7
```

### Level 1

```
[3]
```

Result:

```
[[3]]
```

### Level 2

```
[9,20]
```

Result:

```
[[3],[9,20]]
```

### Level 3

```
[15,7]
```

Result:

```
[[3],[9,20],[15,7]]
```

Return:

```python
[[3], [9,20], [15,7]]
```

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each node is visited once.

### Space Complexity

```
O(n)
```

The queue may contain an entire level of nodes.

---

## Key Takeaways

- Level-order traversal uses BFS.
- Queues are the standard data structure for BFS.
- Process nodes level by level.
- A common BFS pattern is:
  - Initialize queue
  - Process current level
  - Add children
  - Repeat until empty.