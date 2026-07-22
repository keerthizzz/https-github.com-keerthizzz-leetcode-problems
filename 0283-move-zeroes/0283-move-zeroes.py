class Solution:
    def moveZeroes(self, nums):
        lastNonZeroFoundAt = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
