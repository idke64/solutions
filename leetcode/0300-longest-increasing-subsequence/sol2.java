class Solution {
    public int lengthOfLIS(int[] nums) {
        int largest = 1;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0,Integer.MIN_VALUE);
        map.put(1,nums[0]);
        int highestSS = 1;
        for (int i = 1; i < nums.length; i++){
            int dp = 0;
            for (int j = highestSS; j >= 0; j--){
                if (nums[i] > map.get(j)){
                    dp = j + 1;
                    if (map.containsKey(j+1)){
                        map.put(dp,Math.min(nums[i],map.get(dp)));
                    }
                    else{
                        map.put(dp, nums[i]);
                    }
                    
                    highestSS = Math.max(highestSS, dp);
                    break;
                }
            }
            largest = Math.max(largest,dp);
        }
        return largest;
    }
}