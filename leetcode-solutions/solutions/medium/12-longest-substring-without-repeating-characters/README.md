# 3. Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.

## Approach

This solution uses the **sliding window** technique with a **set** to track unique characters currently in the window.

The algorithm:

1. Initialize an empty set called `seen`.
2. Create a pointer `left` to represent the start of the current window.
3. Iterate through the string using a pointer `right`.
4. If the current character already exists in `seen`:
   - Remove characters from the left side of the window.
   - Move `left` forward until the duplicate is removed.
5. Add the current character to `seen`.
6. Calculate the current window length.
7. Update the longest substring length found so far.
8. Return the maximum length.

This ensures the window always contains unique characters.

## Example

Input:

```python
s = "abcabcbb"
```

Output:

```python
3
```

Explanation:

```text
Window: "abc"
Length: 3

The longest substring without repeating characters is "abc".
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(min(n, m))

Where:

- n = length of the string
- m = size of the character set

## Key Concepts

* Strings
* Sliding Window
* Two Pointers
* Hash Set
* Character Tracking