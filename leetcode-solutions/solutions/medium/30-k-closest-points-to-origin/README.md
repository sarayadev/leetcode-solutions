# 973. K Closest Points to Origin

## Problem

Given an array of points where:

```python
points[i] = [xi, yi]
```

Return the `k` points closest to the origin `(0,0)`.

The distance between a point and the origin is:

```python
√(x² + y²)
```

You may return the answer in any order.

---

## Key Idea

We need the `k` smallest distances.

A **Min Heap** allows us to efficiently retrieve points with the smallest distance.

Since square roots do not affect ordering, we use:

```python
x² + y²
```

instead of:

```python
√(x² + y²)
```

---

## Approach

1. Calculate each point's squared distance from the origin
2. Store `(distance, point)` in a min heap
3. Remove the smallest element `k` times
4. Return the collected points

---

## Algorithm

1. Create an empty heap
2. For each point:
   - Calculate `x² + y²`
   - Push into heap
3. Pop from heap `k` times
4. Return the points

---

## Code

```python
import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (distance, [x, y]))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
```

---

## Dry Run

Input:

```python
points = [[1,3],[-2,2]]
k = 1
```

### Distances

```python
[1,3]   -> 1² + 3² = 10
[-2,2]  -> (-2)² + 2² = 8
```

Heap:

```python
[(8,[-2,2]), (10,[1,3])]
```

### Pop 1 Time

Remove:

```python
[-2,2]
```

Return:

```python
[[-2,2]]
```

---

## Complexity Analysis

### Time Complexity

```python
O(n log n)
```

Each insertion into the heap takes `O(log n)`.

### Space Complexity

```python
O(n)
```

The heap stores all points.

---

## Key Takeaways

- Distance comparisons do not require square roots.
- Min heaps efficiently retrieve the smallest values.
- Store `(distance, point)` pairs.
- Useful pattern for Top K problems.

---