class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        sorted_nums = sorted(nums)

        max_streak = 0
        count = 1

        for i in range(len(sorted_nums) - 1):
            if abs(sorted_nums[i+1] - sorted_nums[i]) == 1:
                count += 1
            elif abs(sorted_nums[i+1] - sorted_nums[i]) > 1:
                count = 1
                
            max_streak = max(max_streak, count)
        
        return max_streak
