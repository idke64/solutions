class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        max_count = 1
        slope_b = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                slope = ""
                b = ""
                if dx == 0:
                    slope += "n"
                    b += str(points[i][0])
                else:
                    slope += str(dy/dx)
                    b += str(points[i][1] - (dy/dx) * points[i][0])
                if slope + b not in slope_b:
                    slope_b[slope + b] = {i, j}
                else:
                    slope_b[slope + b].add(i)
                    slope_b[slope + b].add(j)
                max_count = max(len(slope_b[slope + b]), max_count)
        return max_count