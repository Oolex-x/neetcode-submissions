class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL, maxR, water = height[l], height[r], 0

        while l < r:

            if maxR < maxL:
                water += max(0,(maxR -  height[r]))
                r -= 1
                maxR = max(height[r], maxR)
            else:
                water += max(0,(maxL -  height[l]))
                l += 1
                maxL = max(height[l], maxL)

        return water