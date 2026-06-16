# 11. Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`.

There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the most water.

Return the maximum amount of water a container can store.

## Approach

This solution uses the **Two Pointers** pattern.

The algorithm:

1. Initialize two pointers:
   - `left` at the beginning of the array.
   - `right` at the end of the array.
2. Calculate the area formed by the two lines:
   - Width = `right - left`
   - Height = `min(height[left], height[right])`
   - Area = Width × Height
3. Track the maximum area found.
4. Move the pointer with the smaller height inward.
   - The shorter line limits the amount of water that can be stored.
   - Moving the taller line cannot increase the container's height.
5. Continue until the pointers meet.

## Example

Input:

```python
height = [1,8,6,2,5,4,8,3,7]
```

Output:

```python
49
```

Explanation:

```text
left = 1 (height = 8)
right = 8 (height = 7)

width = 7
height = min(8, 7) = 7

area = 7 × 7 = 49
```

This is the maximum area possible.

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

Where:

- n = length of the array

## Key Concepts

* Two Pointers
* Arrays
* Greedy Optimization
* Area Calculation