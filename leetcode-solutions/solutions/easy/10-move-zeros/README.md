# 283. Move Zeroes

## Problem Statement

Given an integer array `nums`, move all `0`’s to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

## Approach

This solution uses a two pointers (in-place) approach.

The algorithm:

Initialize a pointer `left = 0` to track the position for the next non-zero element.
Iterate through the array with index `i`.
If `nums[i]` is not zero:
Swap `nums[i]` with `nums[left]`
Increment `left`
Continue until the end of the array.
All non-zero elements are moved to the front while zeros naturally shift to the end.
This ensures the relative order of non-zero elements is preserved while pushing all zeros to the back in a single pass.

## Example

Input:

```python
nums = [0, 1, 0, 3, 12]
```

Output:

```python
[1, 3, 12, 0, 0]
```

Explanation:

```text
Step by step:
[0, 1, 0, 3, 12] → swap 1 forward
[1, 0, 0, 3, 12] → swap 3 forward
[1, 3, 0, 0, 12] → swap 12 forward
[1, 3, 12, 0, 0]
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

## Key Concepts

Arrays
Two Pointers
In-place Manipulation
Stable Ordering