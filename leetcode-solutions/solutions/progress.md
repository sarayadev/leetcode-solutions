# Progress Tracker

## Easy

- [x] Two Sum
  - Pattern: Hash Map
  - Learned: Using a dictionary for O(1) lookups and complement-based searching.

- [x] Contains Duplicate
  - Pattern: Hash Set
  - Learned: Using sets to efficiently detect duplicate values and understand unique value storage.

- [x] Valid Anagram
  - Pattern: Sorting
  - Learned: Using sorted strings to compare character frequencies and determine if two strings are anagrams.

- [x] Best Time to Buy and Sell Stock
  - Pattern: Greedy, One Pass
  - Learned: Tracking the lowest price seen so far and calculating the maximum profit at each step allows the problem to be solved in O(n) time.

- [x] Running Sum of 1D Array
  - Pattern: Prefix Sum
  - Learned: Building cumulative sums while traversing an array and understanding how previous values can be reused efficiently.

- [x] Find Pivot Index
  - Pattern: Prefix Sum
  - Learned: Using running totals to compare left and right sums without repeatedly recalculating subarrays.

- [x] Move Zeroes
  - Pattern: Two Pointers, In-place
  - Learned: Moving all non-zero elements forward while maintaining the relative order of the non-zero elements and filling remaining positions with zeros.

- [x] Valid Palindrome
  - Pattern: String Manipulation, Two Pointers
  - Learned: Cleaning strings by removing non-alphanumeric characters, converting characters to lowercase, and comparing the cleaned string to its reverse to verify palindrome properties.

- [x] Roman to Integer
  - Pattern: Hash Map, String Traversal
  - Learned: Using a dictionary to map Roman numerals to integer values and handling subtraction cases by comparing adjacent characters while traversing the string.

- [x] Longest Common Prefix
  - Pattern: String Traversal, Prefix Matching
  - Learned: Using the first string as a reference prefix and progressively shortening it until it matches the beginning of every string in the array.

- [x] Is Subsequence
  - Pattern: Two Pointers
  - Learned: Using two pointers to efficiently determine whether one string appears within another while maintaining character order.

- [ ] Valid Parentheses

## Medium

- [x] Group Anagrams
  - Pattern: Hash Map, Sorting
  - Learned: Using sorted strings as dictionary keys to group related data and organize anagrams efficiently.

- [x] Top K Frequent Elements
  - Pattern: Hash Map, Bucket Sort
  - Learned: Using frequency counting and bucket sort to achieve O(n) performance.

- [x] Product of Array Except Self
  - Pattern: Prefix Product, Suffix Product
  - Learned: Using left and right cumulative products to solve array problems in O(n) time without division and with constant extra space.

- [x] Longest Substring Without Repeating Characters
  - Pattern: Sliding Window, Hash Set
  - Learned: Maintaining a dynamic window of unique characters while efficiently removing duplicates and tracking the maximum substring length.

- [x] Container With Most Water
  - Pattern: Two Pointers
  - Learned: Starting with the widest container and moving the shorter pointer inward efficiently finds the maximum area in O(n) time.
     
 - [x] 3Sum
  - Pattern: Sorting, Two Pointers
  - Learned: Sorting enables efficient two-pointer scanning for triplets. Avoiding duplicates is key to preventing repeated results.
## Hard

- [ ] None yet

---

# Progress Summary

Easy: 11 completed

Medium: 6 completed

Hard: 0 completed

Total Problems Solved: 17

---

# Notes

## June 1, 2026
Completed Two Sum.

### Key Takeaways

- Learned how hash maps can reduce time complexity from O(n²) to O(n).
- Improved understanding of dictionary lookups.
- Practiced identifying complements while iterating through an array.

## June 2, 2026
Completed Contains Duplicate.

### Key Takeaways

- Learned how sets automatically remove duplicate values.
- Reinforced understanding of hash-based data structures.
- Practiced identifying duplicates in O(n) time.

## June 3, 2026
Completed Valid Anagram.

### Key Takeaways

- Learned how sorting can be used to compare character frequencies.
- Practiced working with strings and character ordering.
- Reinforced understanding of how anagrams contain the same characters in different arrangements.

## June 4, 2026
Completed Group Anagrams.

### Key Takeaways

- Learned how hash maps can be used to group related values.
- Practiced combining sorting with dictionaries to solve problems efficiently.
- Improved understanding of using transformed data as dictionary keys.
- Reinforced time complexity analysis involving sorting operations.

## June 5, 2026
Completed Top K Frequent Elements.

### Key Takeaways

- Learned how to count frequencies using hash maps.
- Practiced using bucket sort for linear-time solutions.
- Improved understanding of frequency-based problems.
- Reinforced O(n) time complexity optimization techniques.

## June 6, 2026
Completed Product of Array Except Self.

### Key Takeaways

- Learned how prefix products store the product of all elements to the left.
- Learned how suffix products store the product of all elements to the right.
- Practiced solving array problems without using division.
- Improved understanding of space optimization techniques.
- Reinforced the concept of multiple passes through an array while maintaining O(n) time complexity.

## June 7, 2026
Completed Best Time to Buy and Sell Stock.

### Key Takeaways

- Learned how greedy algorithms make locally optimal decisions.
- Practiced tracking a running minimum value while iterating through an array.
- Improved understanding of profit calculations using previous values.
- Reinforced solving array problems in O(n) time with O(1) extra space.
- Learned how to identify opportunities for optimization without nested loops.

## June 8, 2026
Completed Running Sum of 1D Array.

### Key Takeaways

- Learned how prefix sums accumulate values across an array.
- Practiced updating values in-place for space efficiency.
- Improved understanding of cumulative calculations.
- Reinforced one-pass array traversal techniques.

## June 9, 2026
Completed Find Pivot Index.

### Key Takeaways

- Learned how total sums and running sums can be combined to avoid nested loops.
- Practiced comparing left and right partitions of an array efficiently.
- Improved understanding of prefix sum applications.
- Reinforced solving array problems in O(n) time with O(1) extra space.

## June 10, 2026
Completed Move Zeroes.

### Key Takeaways

- Learned how two pointers can separate zero and non-zero elements efficiently.
- Practiced in-place array manipulation without extra memory.
- Improved understanding of maintaining relative order while rearranging elements.
- Reinforced O(n) time complexity with O(1) space solutions.

## June 11, 2026
Completed Valid Palindrome.

### Key Takeaways

- Learned how to clean and normalize strings before processing.
- Practiced filtering alphanumeric characters and converting characters to lowercase.
- Improved understanding of palindrome checking using string reversal.
- Reinforced string manipulation techniques and character validation.

## June 12, 2026
Completed Longest Substring Without Repeating Characters.

### Key Takeaways

- Learned how the sliding window pattern dynamically expands and shrinks based on conditions.
- Practiced using a hash set to maintain unique characters within a window.
- Improved understanding of two-pointer techniques for substring problems.
- Reinforced O(n) solutions by ensuring each character is processed efficiently.
- Learned how to handle duplicates without restarting the search.

## June 13, 2026
Completed Roman to Integer.

### Key Takeaways

- Learned how to use a hash map (dictionary) to store Roman numeral values.
- Practiced traversing a string with a pointer.
- Improved understanding of handling special subtraction cases such as IV, IX, XL, XC, CD, and CM.
- Reinforced comparing adjacent characters to determine whether to add or subtract values.
- Practiced solving string-processing problems in O(n) time with O(1) extra space.

## June 14, 2026
Completed Longest Common Prefix.

### Key Takeaways

- Learned how to compare multiple strings using a shared prefix.
- Practiced progressively shortening a candidate prefix until it matches all strings.
- Improved understanding of string traversal and prefix-based algorithms.
- Reinforced efficient string comparison techniques without unnecessary extra space.
- Practiced solving string problems in O(S) time, where S is the total number of characters across all strings.

## June 15, 2026
Completed Is Subsequence.

### Key Takeaways

- Learned how to use two pointers to traverse two strings simultaneously.
- Practiced matching characters while maintaining their relative order.
- Improved understanding of subsequences and ordered character matching.
- Reinforced solving string problems in O(n) time with O(1) extra space.
- Strengthened understanding of the Two Pointers pattern for string traversal problems.

## June 16, 2026
Completed Container With Most Water.

### Key Takeaways

- Learned how the Two Pointers pattern can reduce a brute-force O(n²) solution to O(n).
- Practiced calculating area using width × minimum height.
- Improved understanding of why moving the shorter pointer is optimal.
- Reinforced greedy decision-making while traversing an array.
- Strengthened problem-solving skills involving maximizing values under constraints.

## June 17, 2026
Completed 3Sum.

### Key Takeaways
- Learned how sorting reduces brute force complexity.
- Used two pointers to find triplets summing to zero.
- Practiced duplicate skipping to avoid repeated results.
- Extended two-pointer technique from pairs to triplets.
