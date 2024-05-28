class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int largest = 1;
        for (int i = 1; i < nums.length; i++){
            int max = 1;
            for (int j = 0; j < i; j++){
                if (nums[i] > nums[j]){
                    max = Math.max(dp[j] + 1, max);
                }
            }
            largest = Math.max(largest,max);
            dp[i] = max;
        }
        return largest;
    }
}