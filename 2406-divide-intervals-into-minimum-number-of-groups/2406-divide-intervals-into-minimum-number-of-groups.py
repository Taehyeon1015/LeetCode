class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        left = sorted([interval[0] for interval in intervals])
        right = sorted([interval[1] for interval in intervals])

        result, current = 1, 1
        i, j = 1, 0
        while i < len(intervals) and j < len(intervals):
            if left[i] <= right[j]:
                current += 1
                i += 1
            else:
                current -= 1
                j += 1
            result = max(result, current)

        return result
