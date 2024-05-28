class Solution {
    public int checkRecord(int n) {
        long[] dp = new long[n];
        long[] a = new long[n];
        long[] l = new long[n];
        long[] ll = new long[n];
        long[] all = new long[n];
        long[] al = new long[n];
        dp[0] = 3;
        a[0] = 1;
        l[0] = 1;
        for (int i = 1; i < n; i++){
            long ps = dp[i-1]; //add p
            long as = modulo(dp[i-1] - a[i-1]); //add a
            long ls = modulo(dp[i-1] - ll[i-1]); //add l

            dp[i] = modulo(ps + as + ls);
            a[i] = modulo(a[i-1] + as + (a[i-1] - all[i-1]));
            all[i] = al[i-1];
            al[i] = modulo(a[i-1] - al[i-1] - all[i-1]);
            l[i] = modulo(ls - l[i-1]);
            ll[i] = l[i-1];    
        }

        return (int) dp[n - 1];
    }
    public static long modulo(long n){
        return ((n % 1000000007) + 1000000007) % 1000000007;
    }
}