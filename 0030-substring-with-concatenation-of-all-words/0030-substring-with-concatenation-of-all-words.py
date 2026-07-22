from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        
        res = []
        n = len(s)
        
        for offset in range(word_len):
            left = offset
            right = offset
            seen = Counter()
            count = 0
            
            while right + word_len <= n:
                word = s[right:right+word_len]
                right += word_len
                
                if word in word_map:
                    seen[word] += 1
                    count += 1
                    
                    while seen[word] > word_map[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right
        
        return res
