class Solution:
    def sumOfUnique(self, nums):
        from collections import Counter
        count = Counter(nums)
        total = 0
        for num, freq in count.items():
            if freq == 1:
                total += num
        return total


        