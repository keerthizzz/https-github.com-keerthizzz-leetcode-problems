class Solution:
    def sequentialDigits(self, low: int, high: int):
        s = "123456789"
        res = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(0, 10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    res.append(num)
        return res
