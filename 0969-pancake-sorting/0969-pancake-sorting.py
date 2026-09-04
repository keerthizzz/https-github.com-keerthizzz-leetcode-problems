class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []

        for size in range(len(arr), 1, -1):
            i = arr.index(size)

            if i != size - 1:
                if i != 0:
                    arr[:i+1] = arr[:i+1][::-1]
                    ans.append(i + 1)

                arr[:size] = arr[:size][::-1]
                ans.append(size)

        return ans
        