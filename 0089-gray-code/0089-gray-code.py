class Solution:
    def grayCode(self, n: int):
        result = [0]
        for i in range(n):
            reflected = [x | (1 << i) for x in reversed(result)]
            result += reflected
        return result
