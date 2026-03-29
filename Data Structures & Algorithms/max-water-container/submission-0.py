class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            r = len(heights) - 1
            while i < r:
                area = (r - i) * min(heights[i], heights[r])
                maxArea =  max(maxArea, area)
                r -= 1
        return maxArea