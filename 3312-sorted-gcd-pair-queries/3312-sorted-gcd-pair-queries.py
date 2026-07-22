import bisect

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        cnt = [0] * (max_val + 1)

        for num in nums:
            cnt[num] += 1

        for d in range(1, max_val + 1):
            for multiple in range(2 * d, max_val + 1, d):
                cnt[d] += cnt[multiple]

        freq = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total_pairs = cnt[d] * (cnt[d] - 1) // 2
            for multiple in range(2 * d, max_val + 1, d):
                total_pairs -= freq[multiple]
            freq[d] = total_pairs

        prefix = []
        values = []
        running = 0
        for d in range(1, max_val + 1):
            if freq[d] > 0:
                running += freq[d]
                prefix.append(running)
                values.append(d)

        ans = []
        for q in queries:
            idx = bisect.bisect_left(prefix, q + 1)  
            ans.append(values[idx])
        return ans
