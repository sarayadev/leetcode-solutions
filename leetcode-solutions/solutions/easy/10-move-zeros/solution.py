# Solution

class Solution:
    def moveZeroes(self, nums):
        result = []
        zeros = []

        for num in nums:
            if num == 0:
                zeros.append(num)
            else:
                result.append(num)
        nums[:] = result + zeros
