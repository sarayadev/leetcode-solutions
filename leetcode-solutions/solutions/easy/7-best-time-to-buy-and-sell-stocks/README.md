# 121. Best Time to Buy and Sell Stock

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and a different future day to sell that stock.

Return the maximum profit you can achieve. If no profit can be made, return `0`.

## Approach

This solution uses a greedy one-pass approach.

Instead of checking every possible buy and sell combination, the algorithm keeps track of:

- The lowest stock price seen so far
- The maximum profit seen so far

The process is:

1. Initialize the lowest price as the first price in the array.
2. Initialize the maximum profit as `0`.
3. Traverse through the array once.
4. Update the lowest price whenever a smaller value is found.
5. Calculate the profit if the stock were sold on the current day.
6. Update the maximum profit if a larger profit is found.
7. Return the maximum profit.

## Example

Input:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Output:

```python
5
```

Explanation:

```python
Buy at 1
Sell at 6

Profit = 6 - 1 = 5
```

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(1)

## Key Concepts

- Arrays
- Greedy Algorithms
- One-Pass Traversal
- Running Minimum
- Space Optimization