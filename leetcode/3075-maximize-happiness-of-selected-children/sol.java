class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long sum = 0;
        int kCount = -1;
        for (int i = happiness.length - 1; i >= happiness.length - k; i--){
            if (happiness[i] <= happiness.length - i - 1){
                break;
            }
            sum += happiness[i] - (happiness.length - 1 - i);
            
        }
        return sum;
    }
}