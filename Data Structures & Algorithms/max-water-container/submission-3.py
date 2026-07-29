class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        i, j = 0, len(heights) - 1
        
        while i < j:
            dist = j - i    
            height = min(heights[i], heights[j])
            cur = height * dist
            curMax = max(curMax, cur)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return curMax