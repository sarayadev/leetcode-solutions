# 155. Min Stack

## Problem

Design a stack that supports the following operations:

```python
push(val)
pop()
top()
getMin()
```

All operations must run in:

```text
O(1)
```

time.

---

# Example

```python
minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)

minStack.getMin()
```

Output:

```python
-3
```

```python
minStack.pop()
minStack.top()
```

Output:

```python
0
```

```python
minStack.getMin()
```

Output:

```python
-2
```

---

# Intuition

A normal stack can easily provide:

- Push
- Pop
- Top

in constant time.

The challenge is:

```python
getMin()
```

A naive approach would search the entire stack for the minimum value:

```python
min(stack)
```

However, this takes:

```text
O(n)
```

which violates the problem requirements.

Instead, we need a way to always know the current minimum value instantly.

---

# Approach

Use two stacks:

### Main Stack

Stores all values normally.

```python
self.stack
```

### Minimum Stack

Stores the minimum value seen so far at each position.

```python
self.min_stack
```

When pushing:

```python
push(5)
```

Both stacks store:

```python
stack = [5]
min_stack = [5]
```

When pushing:

```python
push(3)
```

The new minimum becomes:

```python
min(3, 5) = 3
```

```python
stack = [5, 3]
min_stack = [5, 3]
```

When pushing:

```python
push(7)
```

The minimum stays:

```python
min(7, 3) = 3
```

```python
stack = [5, 3, 7]
min_stack = [5, 3, 3]
```

The top of `min_stack` always contains the current minimum value.

---

# Solution

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

# Complexity Analysis

## Time Complexity

### push()

```text
O(1)
```

### pop()

```text
O(1)
```

### top()

```text
O(1)
```

### getMin()

```text
O(1)
```

All operations execute in constant time.

---

## Space Complexity

```text
O(n)
```

Both stacks can store up to `n` elements.

---

# Pattern Recognition

**Pattern:** Stack + Auxiliary Stack

Use this pattern when:

- You need normal stack operations.
- Additional information must be retrieved in O(1).
- The extra information can be tracked alongside each stack state.

Common examples:

- Min Stack
- Max Stack
- Frequency Stack
- Browser History
- Undo/Redo Systems

---

# What I Learned

- How to maintain additional state using a second stack.
- How to track the minimum value without scanning the entire stack.
- Why storing the minimum at every position allows O(1) retrieval.
- How auxiliary data structures can improve operation efficiency.
- How stack-based designs often trade extra space for faster lookups.
