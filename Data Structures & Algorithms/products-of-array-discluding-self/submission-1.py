class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [0] * len(nums)
        before[0] = 1

        after = [0] * len(nums)
        after[len(nums)-1] = 1

        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i + 1] * nums[i+1]

        res = []

        for i in range(len(nums)):
            res.append(before[i] * after[i])

        return res