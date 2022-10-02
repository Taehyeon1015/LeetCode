class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num % 2 != 0:
                continue
            
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        # Get sorted array of key, value pair.
        # Example: {0: 1, 2: 2, 4: 2} -> [(2, 2), (4, 2), (0, 1)]
        counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        if not counts:
            return -1
        return counts[0][0]
