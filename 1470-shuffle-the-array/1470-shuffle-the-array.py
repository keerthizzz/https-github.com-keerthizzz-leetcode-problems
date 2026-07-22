from typing import List

class Solution:
    def shuffle(self, num: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(num[i])
            result.append(num[i+n])   
        return result
