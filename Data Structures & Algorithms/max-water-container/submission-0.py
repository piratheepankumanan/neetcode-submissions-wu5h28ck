class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_v= 0
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            max_v = max(max_v, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_v
                
