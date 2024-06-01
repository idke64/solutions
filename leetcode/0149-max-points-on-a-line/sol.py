class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def same_line(point1: List[int], point2: List[int], point3: List[int]) -> bool:
            dx = point1[0] - point2[0]
            dy = point1[1] - point2[1]

            dx3 = point3[0] - point2[0]
            dy3 = point3[1] - point2[1]

            if dx == 0 or dx3 == 0:
                if dx == 0 and dx3 == 0:
                    return True
                else:
                    return False
            if dy/dx == dy3/dx3:
                return True
            return False 
        max_count = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                count = 2
                for k in range(j + 1, len(points)):
                    if same_line(points[i],points[j],points[k]):
                        count += 1
                max_count = max(max_count,count)
        return max_count
        