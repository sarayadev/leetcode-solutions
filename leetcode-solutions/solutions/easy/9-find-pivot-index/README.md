# 724. Find Pivot Index

## Problem Statement

Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.

If no such index exists, return `-1`.

If there are multiple pivot indexes, return the leftmost pivot index.

## Approach

This solution uses a running sum (prefix sum) approach.

The algorithm:

1. Calculate the total sum of the array.
2. Initialize a variable to store the left-side sum.
3. Traverse through the array.
4. Calculate the right-side sum using:

```python
right_sum = total - left_sum - nums[i]
```

5. Compare the left and right sums.
6. If they are equal, return the current index.
7. Otherwise, add the current value to the left sum and continue.
8. If no pivot index is found, return `-1`.

This allows the solution to find the pivot index in a single pass through the array.

## Example

Input:

```python
nums = [1, 7, 3, 6, 5, 6]
```

Output:

```python
3
```

Explanation:

```text
Index 3:
Left Sum = 1 + 7 + 3 = 11
Right Sum = 5 + 6 = 11
```

Since the left and right sums are equal, index 3 is the pivot index.

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

## Key Concepts

- Arrays
- Prefix Sum
- Running Sum
- One-Pass Traversal