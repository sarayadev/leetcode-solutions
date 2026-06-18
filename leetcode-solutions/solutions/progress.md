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
  - Learned: Cleaning strings by removing non-alphanumeric characters, converting characters to lowercase, and comparing the cleaned string to its reverse.

- [x] Roman to Integer
  - Pattern: Hash Map, String Traversal
  - Learned: Using a dictionary to map Roman numerals and handling subtraction cases by comparing adjacent characters.

- [x] Longest Common Prefix
  - Pattern: String Traversal, Prefix Matching
  - Learned: Using the first string as a reference prefix and shrinking it until it matches all strings.

- [x] Is Subsequence
  - Pattern: Two Pointers
  - Learned: Using two pointers to check if one string appears in another while maintaining order.

- [ ] Valid Parentheses

---

## Medium

- [x] Group Anagrams
  - Pattern: Hash Map, Sorting
  - Learned: Using sorted strings as keys to group anagrams efficiently.

- [x] Top K Frequent Elements
  - Pattern: Hash Map, Bucket Sort
  - Learned: Frequency counting combined with bucket sort to achieve linear-time grouping.

- [x] Product of Array Except Self
  - Pattern: Prefix Product, Suffix Product
  - Learned: Using left and right cumulative products to compute results without division in O(n) time.

- [x] Longest Substring Without Repeating Characters
  - Pattern: Sliding Window, Hash Set
  - Learned: Maintaining a dynamic window of unique characters while tracking maximum length efficiently.

- [x] Container With Most Water
  - Pattern: Two Pointers
  - Learned: Using two pointers from both ends and moving the shorter line inward to maximize area in O(n).

- [x] 3Sum
  - Pattern: Sorting, Two Pointers
  - Learned: Sorting enables efficient two-pointer scanning for triplets. Avoiding duplicates is key to preventing repeated results.

- [x] Permutation in String
  - Pattern: Sliding Window, Hash Map
  - Learned: Using a fixed-size sliding window and character frequency counting to efficiently detect whether a permutation of one string exists within another.

---

## Hard

- [ ] None yet

---

# Progress Summary

Easy: 11 completed 
Medium: 7 completed 
Hard: 0 completed 

Total Problems Solved: 18 

---

# Notes

## June 1, 2026
Completed Two Sum.

### Key Takeaways
- Learned how hash maps reduce O(n²) to O(n).
- Practiced complement-based searching.

## June 2, 2026
Completed Contains Duplicate.

### Key Takeaways
- Learned how sets store unique values.
- Improved duplicate detection in O(n).

## June 3, 2026
Completed Valid Anagram.

### Key Takeaways
- Learned sorting-based string comparison.
- Reinforced frequency equivalence in anagrams.

## June 4, 2026
Completed Group Anagrams.

### Key Takeaways
- Learned grouping with hash maps.
- Used sorted strings as dictionary keys.

## June 5, 2026
Completed Top K Frequent Elements.

### Key Takeaways
- Learned frequency counting with hash maps.
- Used bucket sort for O(n) grouping.

## June 6, 2026
Completed Product of Array Except Self.

### Key Takeaways
- Learned prefix and suffix product arrays.
- Solved without division in O(n).

## June 7, 2026
Completed Best Time to Buy and Sell Stock.

### Key Takeaways
- Learned greedy tracking of minimum price.
- Improved single-pass optimization.

## June 8, 2026
Completed Running Sum of 1D Array.

### Key Takeaways
- Learned prefix sums.
- Practiced in-place array updates.

## June 9, 2026
Completed Find Pivot Index.

### Key Takeaways
- Learned prefix sum partitioning.
- Compared left vs right sums efficiently.

## June 10, 2026
Completed Move Zeroes.

### Key Takeaways
- Learned two-pointer in-place rearrangement.
- Maintained relative order of elements.

## June 11, 2026
Completed Valid Palindrome.

### Key Takeaways
- Learned string cleaning and normalization.
- Used two pointers for comparison.

## June 12, 2026
Completed Longest Substring Without Repeating Characters.

### Key Takeaways
- Learned sliding window technique.
- Maintained unique character window.

## June 13, 2026
Completed Roman to Integer.

### Key Takeaways
- Learned hash map mapping for numerals.
- Handled subtraction rules in traversal.

## June 14, 2026
Completed Longest Common Prefix.

### Key Takeaways
- Learned prefix trimming across strings.
- Compared multiple strings efficiently.

## June 15, 2026
Completed Is Subsequence.

### Key Takeaways
- Learned ordered two-pointer matching.
- Checked subsequence relationships.

## June 16, 2026
Completed Container With Most Water.

### Key Takeaways
- Learned greedy two-pointer optimization.
- Maximized area by moving shorter pointer.

## June 17, 2026
Completed 3Sum.

### Key Takeaways
- Learned how sorting reduces brute force complexity.
- Used two pointers to find triplets summing to zero.
- Practiced duplicate skipping to avoid repeated results.
- Extended two-pointer technique from pairs to triplets.

## June 18, 2026
Completed Permutation in String.

### Key Takeaways
- Learned fixed-size sliding window techniques.
- Practiced character frequency counting with hash maps.
- Learned how to update a window incrementally instead of rebuilding counts.
- Reinforced anagram and permutation detection concepts.
- Improved understanding of sliding window optimization for string problems.

---

# Pattern Coverage

## Hash Map
- Two Sum
- Roman to Integer
- Group Anagrams
- Top K Frequent Elements
- Permutation in String

## Hash Set
- Contains Duplicate
- Longest Substring Without Repeating Characters

## Prefix Sum
- Running Sum of 1D Array
- Find Pivot Index

## Two Pointers
- Move Zeroes
- Valid Palindrome
- Is Subsequence
- Container With Most Water
- 3Sum

## Sliding Window
- Longest Substring Without Repeating Characters
- Permutation in String

## Sorting
- Valid Anagram
- Group Anagrams
- 3Sum

## Greedy
- Best Time to Buy and Sell Stock

## Prefix/Suffix
- Product of Array Except Self

## String Traversal
- Roman to Integer
- Longest Common Prefix
