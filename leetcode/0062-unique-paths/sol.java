class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 && n == 1){
            return 1;
        }
        int big;
        int small;
        if (m > n){
            big = m;
            small = n;
        }
        else{
            big = n;
            small = m;
        }
        //(big -1 + small - 1) choose (small - 1)
        return (int) choose((big - 1) + (small - 1), (small - 1));
        
    }
    public static long choose(int n, int r){
        if (r == 0) return 1;
        return (n * choose(n - 1, r - 1)) / r;
    }
}