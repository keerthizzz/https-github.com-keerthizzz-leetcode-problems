class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        repeated = a
        while len(repeated) < len(b):
            repeated += a
            count += 1
        if b in repeated:
            return count
        if b in repeated + a:
            return count + 1
        return -1
