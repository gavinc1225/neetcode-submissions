class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        @requires target != null
        @modifies None
        @effects None
        @returns pair of indices i and j where nums[i] + nums[j] == target
        @throws None (assumes every input has exactly one pair of indices that satisfy condition)

        Intuition:
        We traverse through nums and calculate the difference between the target
        and the current element. If the difference can be found elsewhere in nums
        then we return the indices of both the current element an the difference.

        In order to lookup the elements we should store nums as a (key, value) pair 
        of index and value. This would allow us to return the indices after the pair
        of elements are found.
        '''

        indexValue = {}

        for i, j in enumerate(nums):
            indexValue[j] = i

        for i, j in enumerate(nums):
            difference = target - nums[i]
            if difference in indexValue and indexValue[difference] != i:
                return [i, indexValue[difference]]

        


        