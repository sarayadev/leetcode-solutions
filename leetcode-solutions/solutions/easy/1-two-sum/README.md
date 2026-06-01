# 1. Two Sum



## Problem Statement



Given an array of integers and a target value, return the indices of two numbers whose sum equals the target.



## Approach



This solution uses a hash map to achieve constant-time lookups.



As the array is traversed:



1. Calculate the complement required to reach the target.

2. Check whether the complement has already been encountered.

3. If found, return both indices.

4. Otherwise, store the current value and index in the hash map.



## Example



Input:



nums = [2, 7, 11, 15]

target = 9



Output:



[0, 1]



## Complexity Analysis



Time Complexity: O(n)



Space Complexity: O(n)



## Key Concepts



- Hash Maps

- Dictionary Lookups

- Single-Pass Iteration
