# 392. Is Subsequence

## Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence is a string that can be derived from another string by deleting some (or no) characters without changing the order of the remaining characters.

## Approach

This solution uses the **Two Pointers** pattern.

The algorithm:

1. Create two pointers:
   - `i` for string `s`
   - `j` for string `t`
2. Traverse both strings.
3. If the characters match:
   - Move `i` forward.
4. Always move `j` forward.
5. Continue until either pointer reaches the end of its string.
6. If `i` reaches the end of `s`, then all characters in `s` were found in order.

## Example

Input:

```python
s = "abc"
t = "ahbgdc"
```

Output:

```python
True
```

Explanation:

```text
a h b g d c
↑   ↑     ↑

All characters of "abc" appear in order.
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

Where:

- n = length of string `t`

## Key Concepts

* Two Pointers
* Strings
* Iteration
* Character Matching