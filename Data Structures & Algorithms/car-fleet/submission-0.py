class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # calculate the time for highest pos car to reach target
        # iterate through rest of positions and calculate their time
        # if time is <= the time before it then pop because it will merge into the same fleet
        pair = [[p,s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

