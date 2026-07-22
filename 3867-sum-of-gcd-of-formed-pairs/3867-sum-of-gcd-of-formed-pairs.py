from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefixGcd = []
        mxi = nums[0]
        for i in range(n):
            mxi = max(mxi, nums[i])
            prefixGcd.append(gcd(nums[i], mxi))
        
        prefixGcd.sort()
        
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total
