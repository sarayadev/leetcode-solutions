# 209. Minimum Size Subarray Sum

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return the minimum length of a contiguous subarray whose sum is greater than or equal to `target`.

Return `0` if no such subarray exists.

## Example

```python
target = 7
nums = [2,3,1,2,4,3]
```

Output:

```python
2
```

Explanation:

```text
[4,3] has a sum of 7 and length 2.
```

---

# Intuition

We need the smallest contiguous subarray whose sum is at least `target`.

Since all numbers are positive:

- Expanding the window increases the sum.
- Shrinking the window decreases the sum.

This makes the Sliding Window pattern efficient.

---

# Approach

1. Initialize:
   - `left = 0`
   - `window_sum = 0`
   - `min_length = inf`

2. Expand the window by moving `right`.

3. Add `nums[right]` to the running sum.

4. While `window_sum >= target`:
   - Update the minimum length.
   - Remove `nums[left]` from the sum.
   - Move `left` forward.

5. Return the minimum length found, or `0` if none exists.

---

# Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(
                    min_length,
                    right - left + 1
                )

                window_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each element enters and leaves the window at most once.

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Pattern Recognition

**Pattern:** Variable-Size Sliding Window

Use this pattern when:

- The problem involves a contiguous subarray or substring.
- You need a minimum or maximum window size.
- The window can grow and shrink based on a condition.

---

# What I Learned

- How to use a variable-size sliding window.
- How to maintain a running sum efficiently.
- How to shrink a window to find the minimum valid length.
- How to optimize a brute-force O(n²) solution to O(n).