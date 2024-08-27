class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 1):
            row = triangle[i]
            next_row = [float('inf') for _ in range(len(row) + 1)]
            for j in range(len(row)):
                next_row[j] = min(next_row[j],row[j] + triangle[i+1][j])
                next_row[j+1] = min(next_row[j+1],row[j] + triangle[i+1][j+1])
            triangle[i+1] = next_row
        return min(triangle[-1])
            

