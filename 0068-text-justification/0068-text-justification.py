class Solution:
    def fullJustify(self, words, maxWidth):
        res, i, n = [], 0, len(words)
        while i < n:
            j, line_len = i, 0
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j]); j += 1
            line_words = words[i:j]
            spaces = maxWidth - sum(len(w) for w in line_words)
            if j == n or len(line_words) == 1:
                line = " ".join(line_words).ljust(maxWidth)
            else:
                q, r = divmod(spaces, len(line_words) - 1)
                line = ""
                for k in range(len(line_words) - 1):
                    line += line_words[k] + " " * (q + (k < r))
                line += line_words[-1]
            res.append(line)
            i = j
        return res
