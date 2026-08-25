class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        p = strs[0]
        for s in strs[1:]:
            while not s.startswith(p):
                p = p[:-1]
        return p
        