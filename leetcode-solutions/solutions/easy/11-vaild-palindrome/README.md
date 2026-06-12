# 125. Valid Palindrome

## Problem Statement

Given a string `s`, determine if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

A palindrome reads the same forward and backward.

## Approach

This solution uses string manipulation.

The algorithm:

1. Initialize an empty string `cleaned`.
2. Iterate through each character in the input string.
3. If the character is alphanumeric:
   - Convert it to lowercase.
   - Add it to `cleaned`.
4. Compare `cleaned` with its reversed version.
5. If they are equal, return `True`; otherwise, return `False`.

This ensures only letters and numbers are considered when checking if the string is a palindrome.

## Example

Input:

```python
s = "A man, a plan, a canal: Panama"
```

Output:

```python
True
```

Explanation:

```text
Original: "A man, a plan, a canal: Panama"
Cleaned:  "amanaplanacanalpanama"
Reverse:  "amanaplanacanalpanama"
Result:   True
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

## Key Concepts

* Strings
* String Manipulation
* Character Validation
* Palindrome Checking