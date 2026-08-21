class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(low: int, high: int) -> int:
            if low >= high:
                return 0
            mid = (low + high) // 2
            count = merge_sort(low, mid) + merge_sort(mid + 1, high)
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            nums[low:high + 1] = sorted(nums[low:high + 1])
            return count
        return merge_sort(0, len(nums) - 1)