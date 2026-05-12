class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr)

            if heights[l] < heights[r]:
                tmp = heights[l]
                while heights[l] <= tmp and l < r:
                    l += 1
            else:
                tmp = heights[r]
                while heights[r] <= tmp and r > l:
                    r -= 1
        return res

