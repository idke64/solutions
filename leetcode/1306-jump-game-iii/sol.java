class Solution {
    public boolean canReach(int[] arr, int start) {
        Queue<Integer> queue = new LinkedList<Integer>();
        ArrayList<Integer> zeros = new ArrayList<Integer>();
        boolean[] visited = new boolean[arr.length];
        for (int i = 0; i < arr.length; i++){
            if (arr[i] == 0){
                zeros.add(i);
            }
        }
        
        queue.add(start);
        while (!queue.isEmpty()){
            int currInd = queue.poll();
            visited[currInd] = true;
            if (currInd - arr[currInd] >= 0 && !visited[currInd - arr[currInd]]){
                queue.add(currInd - arr[currInd]);
            }
            if (currInd + arr[currInd] < arr.length && !visited[currInd + arr[currInd]]){
                queue.add(currInd + arr[currInd]);
            }
        }
        for (int i = 0; i < arr.length; i++){
            System.out.print(visited[i] + " ");
        }
        for (int i = 0; i < zeros.size(); i++){
            if (visited[zeros.get(i)]){
                return true;
            }
        }
        
        return false;
    }
}