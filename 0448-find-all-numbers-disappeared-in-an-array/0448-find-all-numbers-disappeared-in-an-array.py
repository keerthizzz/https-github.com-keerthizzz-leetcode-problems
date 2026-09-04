class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])

        ans = []

        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
        