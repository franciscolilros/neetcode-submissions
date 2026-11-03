class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        temp = [(i, j) for i, j in zip(position, speed)]
        temp.sort()

        stack = []

        for i in temp:
            stack.append((target - i[0]) / i[1])
        
        curr = stack.pop()
        while stack:
            if stack[-1] <= curr:
                stack.pop()
            else:
                res += 1
                curr = stack.pop()
        return res