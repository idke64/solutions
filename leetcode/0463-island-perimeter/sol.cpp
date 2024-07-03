class Solution {
public:
    int ans = 0;
    int islandPerimeter(vector<vector<int>>& grid) {
        vector<vector<bool>> visited(grid.size(), vector<bool> (grid[0].size(), false));
        bool b = false;
        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] == 1){
                    dfs(grid,visited,i,j);
                    b = true;
                    break;
                }
            }
            if (b){
                break;
            }
        }
        
        return ans;
    } 
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y){

        if (visited[x][y]){
            return;
        }
        visited[x][y] = true;
        int count = 0;
        if (x+1 < grid.size() && grid[x+1][y] == 1){
            count++;
            dfs(grid,visited,x+1,y);
        }
        if (x-1 >= 0 && grid[x-1][y] == 1){
            count++;
            dfs(grid,visited,x-1,y);
        }
        if (y+1 < grid[0].size() && grid[x][y+1] == 1){
            count++;
            dfs(grid,visited,x,y+1);
        }
        if (y-1 >= 0 && grid[x][y-1] == 1){
            count++;
            dfs(grid,visited,x,y-1);
        }
        ans += (4 - count);
    
        
    }
};