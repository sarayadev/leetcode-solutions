# 1480. Running Sum of 1D Array

## Problem Statement

Given an array `nums`, return the running sum of `nums`.

The running sum of an array is defined as:

```python
runningSum[i] = sum(nums[0] ... nums[i])
```

In other words, each element in the result is the sum of all previous elements and the current element.

## Approach

This solution uses a running total (prefix sum) approach.

The algorithm:

1. Initialize a variable to store the running total.
2. Create an empty list to store the results.
3. Traverse through the array.
4. Add the current number to the running total.
5. Append the running total to the result list.
6. Return the result list.

This allows the running sum to be calculated in a single pass through the array.

## Example

Input:

```python
nums = [1, 2, 3, 4]
```

Output:

```python
[1, 3, 6, 10]
```

Explanation:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

Result:

```python
[1, 3, 6, 10]
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

## Key Concepts

- Arrays
- Prefix Sum
- Running Total
- One-Pass Traversal