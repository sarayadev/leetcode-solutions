# 20. Valid Parentheses

## Problem

Given a string `s` containing just the characters:

```python
'(', ')', '{', '}', '[' and ']'
```

Determine if the input string is valid.

A string is valid if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

## Example

```python
s = "()[]{}"
```

Output:

```python
True
```

---

# Intuition

The most recently opened bracket must be the first one closed.

Example:

```python
({[]})
```

The brackets close in reverse order:

```text
Open:  (  {  [
Close: ]  }  )
```

This is a Last-In, First-Out (LIFO) process, making a stack the ideal data structure.

---

# Approach

1. Create an empty stack.
2. Create a dictionary mapping closing brackets to opening brackets.
3. Iterate through each character:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - Check if the stack is empty.
     - Pop the top element from the stack.
     - Verify it matches the expected opening bracket.
4. If a mismatch occurs, return `False`.
5. After processing all characters, return `True` only if the stack is empty.

---

# Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each character is pushed and popped from the stack at most once.

## Space Complexity

```text
O(n)
```

In the worst case, all opening brackets are stored in the stack.

---

# Pattern Recognition

**Pattern:** Stack

Use this pattern when:

- Matching opening and closing symbols.
- Processing nested structures.
- Tracking the most recent unresolved element.
- Reversing the order of operations.

Common examples:

- Valid Parentheses
- Min Stack
- Daily Temperatures
- Evaluate Reverse Polish Notation
- Decode String

---

# What I Learned

- How a stack follows the Last-In, First-Out (LIFO) principle.
- How to use a dictionary to efficiently match pairs of brackets.
- How to detect invalid closing brackets immediately.
- Why nested structures are often solved with stacks.
- How to validate matching symbols in a single pass through the string.