# 238. Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that:

```python
answer[i]
```

is equal to the product of all the elements of `nums` except `nums[i]`.

The solution must run in O(n) time and cannot use division.

## Approach

This solution uses prefix and suffix products.

Instead of calculating the product for each position separately, the algorithm keeps track of:

- The product of all elements to the left (prefix product)
- The product of all elements to the right (suffix product)

The process is:

1. Create an output array filled with 1s.
2. Traverse from left to right, storing the prefix product at each index.
3. Traverse from right to left, multiplying each index by the suffix product.
4. Return the completed output array.

## Example

Input:

```python
nums = [1, 2, 3, 4]
```

Output:

```python
[24, 12, 8, 6]
```

Explanation:

```python
24 = 2 * 3 * 4
12 = 1 * 3 * 4
8  = 1 * 2 * 4
6  = 1 * 2 * 3
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

(The output array does not count as extra space.)

## Key Concepts

- Arrays
- Prefix Products
- Suffix Products
- Two-Pass Traversal
- Space Optimization