# 347. Top K Frequent Elements

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

## Approach

This solution uses a hash map to count the frequency of each number and bucket sort to organize numbers by frequency.

The array is traversed once to build a frequency dictionary.

Then:

1. Count the occurrences of each number.
2. Create buckets where the index represents frequency.
3. Place each number into its corresponding bucket.
4. Traverse the buckets from highest frequency to lowest.
5. Collect elements until `k` elements have been found.

## Example

Input:

```python
nums = [1,1,1,2,2,3]
k = 2
```

Output:

```python
[1,2]
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

## Key Concepts

- Hash Maps
- Bucket Sort
- Frequency Counting
- Arrays
