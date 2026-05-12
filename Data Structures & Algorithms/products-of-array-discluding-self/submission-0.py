class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zeroes += 1
        # if there are more than 2 zeroes in the list
        if zeroes > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zeroes == 1:
                if c != 0: res[i] = 0
                else: res[i] = prod
            else:
                res[i] = prod // c
        return res


        