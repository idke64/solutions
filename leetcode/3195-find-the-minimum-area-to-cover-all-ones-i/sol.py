class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = -1
        left = -1
        right = -1
        down = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and top == -1:
                    top = i
                if grid[i][j] == 1:
                    down = i
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1 and left == -1:
                    left = i
                if grid[j][i] == 1:
                    right = i
                    
        print(top,down,right,left)
        return (down - top + 1) * (right - left + 1)