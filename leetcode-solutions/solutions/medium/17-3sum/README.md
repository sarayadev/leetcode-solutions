# 15. 3Sum

## Problem Statement

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

```python
nums[i] + nums[j] + nums[k] == 0
```

The solution set must not contain duplicate triplets.

## Approach

This solution uses the **Sorting + Two Pointers** pattern.

The algorithm:

1. Sort the array.
2. Iterate through the array, treating each number as the first element of a potential triplet.
3. Skip duplicate values for the first element to avoid duplicate triplets.
4. Use two pointers:
   - `left` starts immediately after the current element.
   - `right` starts at the end of the array.
5. Calculate the sum of the three numbers:
   - If the sum is less than `0`, move `left` right.
   - If the sum is greater than `0`, move `right` left.
   - If the sum equals `0`, record the triplet.
6. Skip duplicate values for both pointers after finding a valid triplet.
7. Continue until all unique triplets have been found.

## Example

Input:

```python
nums = [-1,0,1,2,-1,-4]
```

Output:

```python
[[-1,-1,2],[-1,0,1]]
```

Explanation:

```text
Sorted array:
[-4,-1,-1,0,1,2]

Triplet 1:
-1 + -1 + 2 = 0

Triplet 2:
-1 + 0 + 1 = 0
```

These are the only unique triplets whose sum equals zero.

## Complexity Analysis

Time Complexity: O(n²)

Space Complexity: O(1)

Where:

- n = length of the array
- The array is sorted once, then scanned using a two-pointer search for each element.

Note: The output list is not included in the space complexity calculation.

## Key Concepts

* Arrays
* Sorting
* Two Pointers
* Duplicate Handling
* Sum Target Search