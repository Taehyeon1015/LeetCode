class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = set()
        i, j, result = 0, 0, 0
        for c in s:
            if c in memory:
                while s[i] != c:
                    memory.remove(s[i])
                    i += 1
                i += 1
            memory.add(c)
            result = max(result, j - i + 1)
            j += 1
        return result
