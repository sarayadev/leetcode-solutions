# 13. Roman to Integer

## Problem Statement

Roman numerals are represented by seven different symbols:

```text
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

Given a Roman numeral string `s`, convert it to an integer.

Roman numerals are usually written from largest to smallest from left to right. However, some numerals use subtraction:

```text
IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900
```

## Approach

This solution uses a **dictionary** to store Roman numeral values and a **while loop** to process the string.

The algorithm:

1. Create a dictionary that maps Roman numerals to their integer values.
2. Initialize a variable `total` to store the final result.
3. Use a pointer `i` to traverse the string.
4. Check whether the current numeral forms a subtraction pair with the next numeral.
5. If it does:
   - Subtract the current value from the next value.
   - Add the result to `total`.
   - Move the pointer forward by 2 positions.
6. Otherwise:
   - Add the current numeral's value to `total`.
   - Move the pointer forward by 1 position.
7. Continue until the entire string has been processed.
8. Return `total`.

## Example

Input:

```python
s = "MCMXCIV"
```

Output:

```python
1994
```

Explanation:

```text
M = 1000
CM = 900
XC = 90
IV = 4

1000 + 900 + 90 + 4 = 1994
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

Where:

- n = length of the Roman numeral string

## Key Concepts

* Strings
* Hash Map (Dictionary)
* Two Pointers
* Iteration
* Conditional Logic