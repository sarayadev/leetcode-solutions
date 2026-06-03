# 242. Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Approach

This solution uses sorting to compare the characters in both strings.

As the strings are processed:

1. Sort string `s`.
2. Sort string `t`.
3. Compare the sorted results.
4. If they are equal, the strings contain the same characters with the same frequencies.
5. Return the comparison result.

## Example

Input:

s = "anagram"
t = "nagaram"

Output:

True

## Complexity Analysis

Time Complexity: O(n log n)

Space Complexity: O(n)

## Key Concepts

- Sorting
- String Comparison
- Character Frequency
- Anagrams
