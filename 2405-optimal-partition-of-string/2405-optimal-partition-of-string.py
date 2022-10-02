class Solution:
    def partitionString(self, s: str) -> int:
        is_exist = [False for i in range(26)]
        result = 0
        
        for c in s:    
            idx = ord(c) - ord('a')
            if is_exist[idx]:
                result += 1
                is_exist = [False for i in range(26)]

            is_exist[idx] = True
        
        # Add the last substring.
        if any(is_exist):
            result += 1

        return result
