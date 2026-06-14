# 14. Longest Common Prefix

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Approach

This solution uses the **first string as the initial prefix** and compares it with every other string in the array.

The algorithm:

1. Check if the array is empty.
2. Set the first string as the current prefix.
3. Iterate through the remaining strings.
4. While the current string does not start with the prefix:
   - Remove the last character from the prefix.
   - If the prefix becomes empty, return `""`.
5. Continue until all strings have been checked.
6. Return the final prefix.

## Example

Input:

```python
strs = ["flower", "flow", "flight"]
```

Output:

```python
"fl"
```

Explanation:

```text
flower
flow
flight

Common prefix = "fl"
```

## Complexity Analysis

Time Complexity: O(S)

Space Complexity: O(1)

Where:

- S = total number of characters across all strings

## Key Concepts

* Strings
* Iteration
* Prefix Matching
* While Loops