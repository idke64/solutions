class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> l = new ArrayList<List<Integer>>();
        HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();
        l.add(new ArrayList<Integer>());
        for (int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
            List<Integer> temp = new ArrayList<Integer>();
            temp.add(nums[i]);
            l.add(temp);
        }
        int currInd = 1;
        for (int i = 1; i < nums.length; i++){
            int s = l.size();
            for (int j = currInd; j < s; j++){
                
                
                int ind = map.get(l.get(j).get(l.get(j).size() - 1));
                for (int k = ind+1; k < nums.length; k++){
                    List<Integer> temp = new ArrayList<Integer>();
                    for (int z = 0; z < l.get(j).size(); z++) {
                        temp.add(l.get(j).get(z));
                    } 
                    temp.add(nums[k]);
                    
                    l.add(temp);
                }
            }
            
            currInd = s;
        }
        return l;
    }
    public static void print(List<List<Integer>> list){
        for (int i = 0; i < list.size(); i++){
            System.out.print("[");
            for (int j = 0; j < list.get(i).size(); j++){
                System.out.print(list.get(i).get(j) + " ");
            }
            System.out.print("] ");
        }
        System.out.println();
    }
}