class Solution {
    public int climbStairs(int n) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        return fib(n, map);
    }
    public static int fib(int n, HashMap<Integer,Integer> map){
        if (n == 1 || n == 0){
            return 1;
        }
        int first;
        if (map.containsKey(n-1)){
            first = map.get(n-1);
        }
        else{
            first = fib(n-1,map);
        }
        int second = fib(n-2,map);
        map.put(n-2,second);
        return first + second;
    }
}