# 1046. Last Stone Weight

## Problem

You are given an array of stone weights.

Each turn:

1. Choose the two heaviest stones
2. Smash them together

Rules:

- If both stones have the same weight, both are destroyed
- If weights differ, the smaller stone is destroyed and the larger stone becomes:

```python
y - x
```

Return the weight of the last remaining stone.

If no stones remain, return `0`.

---

## Key Idea

We repeatedly need the **largest** stones.

Python only provides a Min Heap, so we simulate a Max Heap by storing negative values.

---

## Approach

1. Convert all stone weights to negatives
2. Build a heap
3. Repeatedly remove the two largest stones
4. If they differ, push the difference back
5. Continue until one or zero stones remain

---

## Algorithm

1. Convert stones to negative numbers
2. Heapify the array
3. While heap has at least two stones:
   - Remove largest stone
   - Remove second largest stone
   - If different, push remaining weight
4. Return remaining stone or `0`

---

## Code

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0
```

---

## Dry Run

Input:

```python
stones = [2,7,4,1,8,1]
```

### Initial Max Heap

```python
[8,7,4,2,1,1]
```

### Smash 8 and 7

```python
8 - 7 = 1
```

Remaining:

```python
[4,2,1,1,1]
```

### Smash 4 and 2

```python
4 - 2 = 2
```

Remaining:

```python
[2,1,1,1]
```

### Smash 2 and 1

```python
2 - 1 = 1
```

Remaining:

```python
[1,1,1]
```

### Smash 1 and 1

Both destroyed.

Remaining:

```python
[1]
```

Return:

```python
1
```

---

## Complexity Analysis

### Time Complexity

```python
O(n log n)
```

Each heap operation takes `O(log n)`.

### Space Complexity

```python
O(n)
```

The heap stores all stones.

---

## Key Takeaways

- Use a Max Heap whenever you repeatedly need the largest element.
- Python simulates a Max Heap using negative values.
- Remove the two largest stones each round.
- Heap problems often involve repeated insertion and removal of extreme values.
