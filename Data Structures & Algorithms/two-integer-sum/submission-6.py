class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {} # value -> index

        for i, n in enumerate(nums): # store all indexes
            output[n] = i

        for i, n in enumerate(nums): #loop through nums
            diff = target - n
            if diff in output and output[diff] != i: # if difference is in the output and it's not this one
                return [i, output[diff]] # return this 
            