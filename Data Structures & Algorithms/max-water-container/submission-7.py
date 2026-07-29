class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        i, j = 0, len(heights) - 1
        
        while i < j:
            cur = (j - i) * min(heights[i], heights[j])
            result = max(result, cur)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return result