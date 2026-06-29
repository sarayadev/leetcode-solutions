# 104. Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root to a leaf node.

---

## Key Idea

The depth of a tree is:

```
1 + max(left depth, right depth)
```

This naturally leads to a recursive solution.

---

## Approach

For each node:

1. Find the depth of the left subtree
2. Find the depth of the right subtree
3. Return the larger depth plus one

Base case:

- If the node is `None`, return `0`

---

## Algorithm

1. If root is `None`, return `0`
2. Recursively calculate left depth
3. Recursively calculate right depth
4. Return `1 + max(left, right)`

---

## Code

```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
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

### Leaf Nodes

```
9 -> depth 1
15 -> depth 1
7 -> depth 1
```

### Node 20

```
1 + max(1,1)
= 2
```

### Root 3

```
1 + max(1,2)
= 3
```

Return:

```
3
```

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

### Space Complexity

```
O(h)
```

Where `h` is the height of the tree.

---

## Key Takeaways

- Tree depth problems are often recursive.
- Think: current node + deepest subtree.
- Base case is an empty tree.

---