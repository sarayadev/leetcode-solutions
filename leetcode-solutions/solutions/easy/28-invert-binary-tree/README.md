# 226. Invert Binary Tree

## Problem

Given the root of a binary tree, invert the tree.

Inverting means swapping every node's left and right children.

---

## Key Idea

For every node:

```
left ↔ right
```

Then recursively invert the subtrees.

---

## Approach

1. Swap the children
2. Invert the left subtree
3. Invert the right subtree

Base case:

- Empty node returns `None`

---

## Algorithm

1. If root is `None`, return `None`
2. Swap left and right
3. Recursively invert children
4. Return root

---

## Code

```python
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

---

## Dry Run

Original:

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

After inversion:

```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

Return inverted tree.

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

---

## Key Takeaways

- Inversion is simply repeated swapping.
- Recursive tree traversal handles every node.
- A classic recursion interview question.

---