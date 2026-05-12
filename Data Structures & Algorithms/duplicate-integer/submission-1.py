class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for n in nums:
            num_dict[n] = 1 + num_dict.get(n, 0)
        
        for n in nums:
            if num_dict[n] > 1:
                return True
        
        return False

        