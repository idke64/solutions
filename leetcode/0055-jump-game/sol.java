class Solution {
    public boolean canJump(int[] nums) {
        ArrayList<Integer> zeros = new ArrayList<Integer>();
        for (int i = 0; i < nums.length - 1; i++){
            if (nums[i] == 0){
                zeros.add(i);
            }
        }
        //edge case 
        if (nums.length == 1){
            return true;
        }
        for (int i = 0; i < zeros.size(); i++){
            boolean pass = false;
            for (int j = 0; j < zeros.get(i); j++){
                if (nums[j] - (zeros.get(i) - j) > 0){
                    //can go past this zero
                    pass = true;
                    break;
                }
            }
            if (!pass){
                return false;
            }
        }
        return true;
    }
}