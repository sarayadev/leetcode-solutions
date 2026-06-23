# 739. Daily Temperatures

## Problem

Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that:

```python
answer[i]
```

is the number of days you have to wait after the `i`th day to get a warmer temperature.

If there is no future day for which this is possible, keep:

```python
0
```

for that position.

---

## Example

### Input

```python
temperatures = [73,74,75,71,69,72,76,73]
```

### Output

```python
[1,1,4,2,1,1,0,0]
```

### Explanation

- Day 0 (73°) → warmer temperature is 74° one day later → `1`
- Day 1 (74°) → warmer temperature is 75° one day later → `1`
- Day 2 (75°) → warmer temperature is 76° four days later → `4`
- Day 3 (71°) → warmer temperature is 72° two days later → `2`
- Day 4 (69°) → warmer temperature is 72° one day later → `1`
- Day 5 (72°) → warmer temperature is 76° one day later → `1`
- Day 6 (76°) → no warmer day exists → `0`
- Day 7 (73°) → no warmer day exists → `0`

---

# Intuition

A brute-force solution would compare every temperature with all future temperatures until a warmer day is found.

For each day:

```python
for i in range(len(temperatures)):
    for j in range(i + 1, len(temperatures)):
```

This approach works but requires:

```text
O(n²)
```

time in the worst case.

We need a more efficient method.

The key observation is that some temperatures are still waiting for a warmer day. Instead of repeatedly checking them, we can store them in a stack until a warmer temperature appears.

This leads to a Monotonic Stack solution.

---

# Approach

Use a stack that stores:

```python
(index, temperature)
```

The stack will be maintained in decreasing temperature order.

When a new temperature is encountered:

```python
temp > stack[-1][1]
```

the current temperature is warmer than the temperature at the top of the stack.

This means we have found the answer for that previous day.

We repeatedly pop temperatures from the stack until the current temperature is no longer warmer than the top of the stack.

For every popped element:

```python
result[previous_index] = current_index - previous_index
```

which gives the number of days waited.

After processing, push the current day onto the stack because it may still need a warmer temperature in the future.

---

# Dry Run

Input:

```python
[73,74,75,71,69,72,76,73]
```

Initialize:

```python
result = [0,0,0,0,0,0,0,0]
stack = []
```

### Day 0 (73)

Push:

```python
stack = [(0,73)]
```

### Day 1 (74)

```python
74 > 73
```

Pop:

```python
result[0] = 1
```

Push:

```python
stack = [(1,74)]
```

### Day 2 (75)

```python
75 > 74
```

Pop:

```python
result[1] = 1
```

Push:

```python
stack = [(2,75)]
```

### Day 3 (71)

```python
71 < 75
```

Push:

```python
stack = [(2,75), (3,71)]
```

### Day 4 (69)

```python
69 < 71
```

Push:

```python
stack = [(2,75), (3,71), (4,69)]
```

### Day 5 (72)

```python
72 > 69
```

Pop:

```python
result[4] = 1
```

```python
72 > 71
```

Pop:

```python
result[3] = 2
```

Push:

```python
stack = [(2,75), (5,72)]
```

### Day 6 (76)

```python
76 > 72
```

Pop:

```python
result[5] = 1
```

```python
76 > 75
```

Pop:

```python
result[2] = 4
```

Push:

```python
stack = [(6,76)]
```

### Day 7 (73)

Push:

```python
stack = [(6,76), (7,73)]
```

No warmer temperatures exist for the remaining elements in the stack, so their values remain `0`.

Final result:

```python
[1,1,4,2,1,1,0,0]
```

---

# Solution

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                result[prev_index] = i - prev_index

            stack.append((i, temp))

        return result
```

---

# Why It Works

The stack stores temperatures that have not yet found a warmer day.

Whenever a warmer temperature appears:

```python
temp > stack[-1][1]
```

we immediately know the answer for the temperature at the top of the stack.

Because each temperature is:

- Pushed onto the stack once
- Popped from the stack once

every element is processed a maximum of two times.

This allows the algorithm to run efficiently in linear time.

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each element is pushed once and popped once.

Although a `while` loop exists, the total number of stack operations across the entire algorithm is at most `2n`.

---

## Space Complexity

```text
O(n)
```

In the worst case, the stack may contain every temperature.

Example:

```python
[80,79,78,77,76]
```

No temperatures are popped until the end.

---

# Pattern Recognition

**Pattern:** Monotonic Decreasing Stack

Use this pattern when a problem asks for:

- Next greater element
- Next warmer temperature
- Next larger value
- Distance to a future larger value
- Previous or next greater/smaller element

Common problems using this pattern:

- Daily Temperatures
- Next Greater Element I
- Next Greater Element II
- Car Fleet
- Largest Rectangle in Histogram
- Trapping Rain Water

---

# Key Takeaways

- Store indices when the answer depends on distance between positions.
- A monotonic stack efficiently tracks unresolved elements.
- The stack remains decreasing by temperature.
- When a larger temperature appears, it resolves one or more previous temperatures.
- Each element is pushed and popped at most once, resulting in an `O(n)` solution.
- Monotonic stacks are commonly used for "next greater element" style problems.

---

# What I Learned

- How to use a monotonic decreasing stack.
- Why indices are stored alongside values.
- How to find the next greater element efficiently.
- How stack-based solutions can reduce time complexity from `O(n²)` to `O(n)`.
- Why each element being pushed and popped once guarantees linear performance.