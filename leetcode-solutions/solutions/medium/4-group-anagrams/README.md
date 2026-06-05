# 49. Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

## Approach

This solution uses a hash map and sorting to group words that are anagrams.

When two words are anagrams, sorting their characters produces the same result. The sorted word can therefore be used as a dictionary key.

The array is traversed once:

1. Sort the characters in each word.
2. Convert the sorted characters into a string key.
3. Check if the key exists in the dictionary.
4. If not, create a new list for that key.
5. Append the original word to the corresponding list.
6. Return all grouped values.

## Example

Input:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

Output:

```python
[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]
```

## Complexity Analysis

Time Complexity: O(n * k log k)

Space Complexity: O(n)

Where:

- n = number of strings
- k = average string length

## Key Concepts

- Hash Maps
- Sorting
- String Manipulation
- Dictionaries
- Anagrams
