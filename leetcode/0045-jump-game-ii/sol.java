class Solution {
    public int jump(int[] nums) {
        Queue<int[]> queue = new LinkedList<int[]>();
        int[] origin = {0, 0, 0};
        boolean[] visited = new boolean[nums.length]; 
        queue.add(origin);
        //[startInd, endInd #jumps]
        int ans = 0;
        while (!queue.isEmpty()){
            int[] curr = queue.poll();
            int startInd = curr[0];
            int endInd = curr[1];
            int jumps = curr[2];
            int furthestJump = 0;
            if (endInd == nums.length - 1){
                ans = jumps;
                break;
            }
            for (int i = startInd; i <= endInd; i++){
                furthestJump = Math.max(Math.min(i + nums[i], nums.length - 1), furthestJump);
            }
            int[] step = {endInd + 1, furthestJump, jumps + 1};
            queue.add(step);
        }
        return ans;
    }
}