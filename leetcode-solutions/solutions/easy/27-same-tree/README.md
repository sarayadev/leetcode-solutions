# 100. Same Tree

## Problem

Given the roots of two binary trees `p` and `q`, determine if they are identical.

Two trees are the same if:

- They have the same structure
- Corresponding nodes have the same values

---

## Key Idea

Compare both trees node by node.

At every step:

- Values must match
- Left subtrees must match
- Right subtrees must match

---

## Approach

Use recursion.

Base cases:

- Both nodes are `None` → True
- One is `None` and the other isn't → False
- Values differ → False

Otherwise recursively compare children.

---

## Algorithm

1. Check base cases
2. Compare node values
3. Recursively compare left children
4. Recursively compare right children
5. Return the combined result

---

## Code

```python
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
```

---

## Dry Run

Trees:

```
    1        1
   / \      / \
  2   3    2   3
```

Compare:

```
1 == 1
2 == 2
3 == 3
```

All nodes match.

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
O(h)
```

---

## Key Takeaways

- Compare structure and values.
- Recursive tree comparisons are very common.
- All corresponding nodes must match.

---