class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # create freq arraylist

        for n in nums:
            count[n] = 1 + count.get(n, 0) # store freq into dict

        for n, c in count.items(): # iterate through dict
            freq[c].append(n) # freq = [frequency, num]

        res = []
        for i in range(len(freq) - 1, 0, -1): # iterate backwards through freq list
            for n in freq[i]: # iterate through freq list
                res.append(n) # add number to result
                if len(res) == k:
                    return res

