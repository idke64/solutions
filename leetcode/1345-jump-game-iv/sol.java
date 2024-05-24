class Solution {
    public int minJumps(int[] arr) {
        Queue<int[]> queue = new LinkedList<int[]>();
        boolean[] visited = new boolean[arr.length];
        int[] origin = {0,0};
        queue.add(origin);
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
        for (int i = 0; i < arr.length; i++){
            if (!map.containsKey(arr[i])){
                ArrayList<Integer> al = new ArrayList<Integer>();
                al.add(i);
                map.put(arr[i],al);
            }
            else{
                ArrayList<Integer> al = map.get(arr[i]);
                al.add(i);
                map.put(arr[i],al);
            }
        }
        
        int ans = 0;
        while (!queue.isEmpty()){
            
            int[] curr = queue.poll();
            int currInd = curr[0];
            int jumps = curr[1];
            
            if (currInd == arr.length - 1){
                ans = jumps;
                break;
            }
            if (currInd + 1 < arr.length && !visited[currInd + 1]){
                int[] step = {currInd + 1, jumps + 1};
                visited[currInd + 1] = true;
                queue.add(step);
            }
            if (currInd - 1 >= 0 && !visited[currInd - 1]){
                int[] step = {currInd - 1, jumps + 1};
                visited[currInd - 1] = true;
                queue.add(step);
            }
            if (map.containsKey(arr[currInd])){
               ArrayList<Integer> al = map.get(arr[currInd]);
                for (int i = 0; i < al.size(); i++){
                    if (!visited[al.get(i)]){
                        int[] step = {al.get(i), jumps + 1};
                        visited[al.get(i)] = true;
                        queue.add(step);
                    }
                    
                } 
            }
            
            map.remove(arr[currInd]);
            
        }
        return ans;
    }
}