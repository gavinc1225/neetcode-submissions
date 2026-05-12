class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {} # value -> index

        for i, num in enumerate(nums): #loop through nums
            if (target - num) in output: # if difference is in the output
                return [output[target-num], i] # return this 
            output[num] = i