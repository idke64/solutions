class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<Character>(); 
        HashMap<Character,Integer> v = new HashMap<Character,Integer>();
        
        String best = "";
        String curr = "";
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
           
            if (!set.contains(c)){
                curr += c;
                set.add(c);
            }
            else{
                if (best.length() < curr.length()){
                    best = curr;
                }
                set.clear();
                curr = "";
                for (int j = v.get(c) + 1; j < i + 1;j ++){
                    curr += s.charAt(j);
                    set.add(s.charAt(j));
                }
            }
            v.put(c,i);
            
        }
        if (best.length() < curr.length()){
            best = curr;
        }
        System.out.println(best);
        return best.length();
    }
}