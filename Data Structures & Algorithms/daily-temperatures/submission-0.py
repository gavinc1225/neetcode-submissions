class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i,t in enumerate(temperatures): # iterate through index and temp 
            while stack and t > stack[-1][0]: # while stack exists and t is greater than temp of last temp
                stackT, stackInd = stack.pop() # store temp and index of top and pop
                res[stackInd] = i - stackInd #
            stack.append((t, i))            

        return res
