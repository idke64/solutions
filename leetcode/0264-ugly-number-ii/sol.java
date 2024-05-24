//O(nlogn)

class Solution {
    public int nthUglyNumber(int n) {
        TreeSet<Long> set = new TreeSet<Long>();
        set.add(Long.valueOf(1));
        int counter = 1;
        for (int i = 0; i < n; i++){
            long sm = set.first();
            if (i == n - 1) return (int) sm;
            set.add(Long.valueOf(sm * 2));
            set.add(Long.valueOf(sm * 3));
            set.add(Long.valueOf(sm * 5));
            set.remove(sm);
            
        }
        return 69;
    }
    
}