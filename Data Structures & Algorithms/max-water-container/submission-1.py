class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        i, j = 0, len(heights) - 1
        for i in range(len(heights)):
            j = len(heights) - 1
            while i < j:
                dist = j - i
                
                height = min(heights[i], heights[j])
                cur = height * dist
                curMax = max(curMax, cur)
                j -= 1

        return curMax