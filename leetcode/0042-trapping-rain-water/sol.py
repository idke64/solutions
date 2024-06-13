class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        highest_ind = height.index(max(height))
        start = 0
        curr = 1
        between = 0
        while start < highest_ind:
            if height[curr] >= height[start]:
                ans += ((curr - start - 1) * height[start]) - between
                between = 0
                start = curr
            else:
                between += height[curr]
            curr += 1
        start = len(height) - 1
        curr = len(height) - 2
        while start > highest_ind:
            if height[curr] >= height[start]:
                ans += ((start - curr - 1) * height[start]) - between
                between = 0
                start = curr
            else:
                between += height[curr]
            curr -= 1
        
        return ans

                
        