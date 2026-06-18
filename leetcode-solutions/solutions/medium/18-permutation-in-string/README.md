# 567. Permutation in String

## Problem

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

In other words, return `True` if one of `s1`'s permutations appears as a substring within `s2`.

## Examples

### Example 1

```python
s1 = "ab"
s2 = "eidbaooo"
```

Output:

```python
True
```

Explanation:

```text
The substring "ba" exists in s2.
"ba" is a permutation of "ab".
```

---

### Example 2

```python
s1 = "ab"
s2 = "eidboaoo"
```

Output:

```python
False
```

Explanation:

```text
No substring of length 2 contains the same character frequencies as "ab".
```

---

## Constraints

```text
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
```

---

# Intuition

A permutation of a string must contain:

1. The same characters
2. The same frequency of each character
3. The same total length

For example:

```text
abc
acb
bac
bca
cab
cba
```

All permutations contain:

```text
a = 1
b = 1
c = 1
```

Since every valid permutation has the same character counts, we can compare character frequencies instead of generating every permutation.

Generating permutations would be extremely expensive.

Instead, we slide a window across `s2` and check whether any window contains the same frequency counts as `s1`.

---

# Approach

## Step 1

Create a frequency map for `s1`.

Example:

```python
s1 = "ab"
```

Frequency map:

```python
{
    'a': 1,
    'b': 1
}
```

---

## Step 2

Create a sliding window in `s2`.

The window size must always equal:

```python
len(s1)
```

For:

```python
s1 = "ab"
s2 = "eidbaooo"
```

Window size:

```python
2
```

Possible windows:

```text
ei
id
db
ba
ao
oo
oo
```

---

## Step 3

Track the frequency count of the current window.

Example:

```python
ei
```

Frequency map:

```python
{
    'e': 1,
    'i': 1
}
```

Not equal to:

```python
{
    'a': 1,
    'b': 1
}
```

Move the window.

---

## Step 4

Continue sliding.

Window:

```python
ba
```

Frequency map:

```python
{
    'b': 1,
    'a': 1
}
```

This matches the frequency map of `s1`.

Return:

```python
True
```

---

# Dry Run

## Input

```python
s1 = "ab"
s2 = "eidbaooo"
```

Target frequency:

```python
{
    'a': 1,
    'b': 1
}
```

---

### Window = "ei"

```python
{
    'e': 1,
    'i': 1
}
```

Match?

```python
False
```

---

### Window = "id"

```python
{
    'i': 1,
    'd': 1
}
```

Match?

```python
False
```

---

### Window = "db"

```python
{
    'd': 1,
    'b': 1
}
```

Match?

```python
False
```

---

### Window = "ba"

```python
{
    'b': 1,
    'a': 1
}
```

Match?

```python
True
```

Return:

```python
True
```

---

# Solution

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            window_count[s2[right]] += 1

            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            if window_count == s1_count:
                return True

        return False
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Where:

```text
n = length of s2
```

Each character enters and leaves the sliding window at most once.

---

## Space Complexity

```text
O(1)
```

Only lowercase English letters are stored.

The frequency maps never exceed 26 characters.

---

# Edge Cases

## s1 longer than s2

```python
s1 = "abcd"
s2 = "ab"
```

Output:

```python
False
```

A permutation cannot fit inside a smaller string.

---

## Exact Match

```python
s1 = "abc"
s2 = "abc"
```

Output:

```python
True
```

The entire string is already a permutation.

---

## Repeated Characters

```python
s1 = "aab"
s2 = "eidbaaao"
```

Output:

```python
True
```

Frequency counts must still match exactly.

---

# Pattern Recognition

This problem teaches the:

## Sliding Window Pattern

Characteristics:

- Fixed-size window
- Move left and right pointers
- Add incoming elements
- Remove outgoing elements
- Avoid recalculating information repeatedly

Common Sliding Window Problems:

- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring

---

# Key Concepts

- Sliding Window
- Hash Map
- Frequency Counting
- String Manipulation
- Two Pointers
- Optimization
- Pattern Recognition

---

# What I Learned

- How to use a fixed-size sliding window
- How to track character frequencies efficiently
- How to compare frequency maps
- How to avoid generating permutations
- How to update a window in O(1) time
- How sliding windows reduce brute-force solutions
- How frequency counting helps solve anagram-related problems efficiently