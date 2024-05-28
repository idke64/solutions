//technically O(nlogn)

class Solution {
    public int lengthOfLIS(int[] nums) {
        int largest = 1;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0,Integer.MIN_VALUE);
        map.put(1,nums[0]);
        int highestSS = 1;
        for (int i = 1; i < nums.length; i++){
            int j = binarySearch(nums[i], map, highestSS) + 1;
            if (map.containsKey(j)){
                map.put(j,Math.min(nums[i],map.get(j)));
            }
            else{
                map.put(j, nums[i]);
            }
            
            highestSS = Math.max(highestSS, j);

            largest = Math.max(largest,j);
        }
        return largest;
    }
    public static int binarySearch(int num, HashMap<Integer, Integer> map, int highestSS){
        int low = 0;
        int high = highestSS;
        while (low <= high){
            int mid = low + (high - low) / 2;
            int midValue = map.get(mid);
            int nextValue = map.getOrDefault(mid + 1, Integer.MAX_VALUE);
            if (num > midValue && num <= nextValue){
                return mid;
            }
            else if (num <= midValue){ 
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
}