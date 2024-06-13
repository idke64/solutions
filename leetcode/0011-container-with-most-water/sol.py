class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        max_water = 0
        while left < right:
            max_water = max((right - left) * min(height[left], height[right]),max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water