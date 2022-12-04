class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i, j = 0, len(sorted_nums) -1
        while sorted_nums[i] + sorted_nums[j] != target:
            if sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1
        
        first = nums.index(sorted_nums[i])
        nums[first] = None
        second = nums.index(sorted_nums[j])

        return [first, second]
