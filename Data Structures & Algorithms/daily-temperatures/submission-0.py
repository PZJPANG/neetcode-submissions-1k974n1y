class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                ans[stackIndex] = index - stackIndex
            stack.append((index, temp))
        return ans
                
            