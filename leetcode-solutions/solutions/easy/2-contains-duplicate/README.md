# 217. Contains Duplicate

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Approach

This solution uses a hash set to identify duplicate values efficiently.

A set only stores unique values. By converting the array into a set, any duplicate values are automatically removed.

The lengths of the original array and the set are then compared:

1. Convert the array to a set.
2. Compare the length of the original array to the length of the set.
3. If the lengths are different, a duplicate exists.
4. If the lengths are the same, all values are unique.

## Example

Input:

nums = [1, 2, 3, 1]

Output:

True

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

## Key Concepts

- Hash Sets
- Duplicate Detection
- Unique Value Storage
- Set Operations