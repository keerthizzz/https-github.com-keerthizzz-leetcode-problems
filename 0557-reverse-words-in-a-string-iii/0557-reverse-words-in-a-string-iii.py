class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []
        for w in words:
            result.append("".join(reversed(w)))
        return " ".join(result)

        