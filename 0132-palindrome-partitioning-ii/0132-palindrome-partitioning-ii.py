class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_pal[i][j] = True
                    else:
                        is_pal[i][j] = is_pal[i+1][j-1]

        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if is_pal[j+1][i])
        return dp[-1]
