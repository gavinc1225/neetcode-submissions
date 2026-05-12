class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {} # value, index

        for i in range(len(nums)):
            counts[nums[i]] = i #value -> index

        for i in range(len(nums)):
            diff = target - nums[i] # look for match

            if (diff in counts and counts[diff] != i) :
                return [i, counts[diff]]