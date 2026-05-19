class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = {}

        for i in range(len(position)):
            cars[position[i]] = speed[i]
        
        sorted_cars = dict(sorted(cars.items(), reverse=True))
        print(sorted_cars)

        for i in sorted_cars:
            stack.append((target - i) / sorted_cars[i])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
