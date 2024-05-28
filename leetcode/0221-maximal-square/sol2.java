//O(n^2 logn)

class Solution {
    public int maximalSquare(char[][] matrix) {
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        int best = 0;
        //2d prefix sum
        int[][] psum = new int[matrix.length][matrix[0].length];
        psum[0][0] = matrix[0][0] - 48;
        for (int i = 1; i < psum[0].length; i++){
            psum[0][i] = psum[0][i - 1] + (matrix[0][i] - 48); 
        }
        for (int i = 1; i < psum.length; i++){
            psum[i][0] = psum[i - 1][0] + (matrix[i][0] - 48); 
        }
        for (int i = 1; i < psum.length; i++){
            for (int j = 1; j < psum[0].length; j++) {
                psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + (matrix[i][j] - 48); 
            }
        }
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (matrix[i][j] == '1' && !visited[i][j]){
                    visited[i][j] = true;

                    int low = 1;
                    int high = Math.min(psum.length - 1 - i, high = psum[0].length - 1 - j);
                    int x = 1;
                    while (low <= high){
                        int mid = low + (high - low) / 2;

                        if ((mid == high && check(psum,i,j,mid) || (check(psum, i, j, mid) && !check(psum, i, j, mid+1)))){
                            x = mid + 1;
                            break;
                        }
                            
                        if (!check(psum, i, j, mid)){
                            high = mid - 1;
                            
                        }
                        else{
                            low = mid + 1;
                        }
                            
                    }
                    
                    if (x * x > best ){
                        best = x * x;
                    }
                }
            }
        }
        return best;
    }
    public static boolean check(int[][] psum, int i, int j, int x){
        int br = psum[i+x][j+x];
        int tl;
        int tr;
        int bl;
        if (i - 1 >= 0 && j - 1 >= 0){
            tl = psum[i-1][j-1];
        }
        else{
            tl = 0;
        }
        if (i - 1 >= 0){
            tr = psum[i-1][j+x];
        }
        else{
            tr = 0;
        }

        if (j - 1 >= 0){
            bl = psum[i+x][j-1];
        }
        else{
            bl = 0;
        }
        int sq = br + tl - bl - tr;
        if (sq != (x+1) * (x+1)){
            return false;
        }
        return true;
    }
}