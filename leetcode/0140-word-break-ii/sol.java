class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<String>();
        for (int i = 0; i < wordDict.size(); i++){
            set.add(wordDict.get(i));
        }
        List<String> ans = new ArrayList<String>();
        solve("", 0, ans, set, s);
        return ans;
    }
    public static void solve(String sentence, int start, List<String> ans, Set<String> set, String s){
        if (start == s.length()){
            ans.add(sentence);
            return;
        }
        String currString = "";
        for (int i = start; i < s.length(); i++){
            currString += s.charAt(i);
            if (set.contains(currString)){
                if (start != 0){
                    solve(sentence + " " + currString, i + 1, ans, set, s);
                }
                else{
                    solve(currString, i + 1, ans, set, s);
                }
                
            }
        }
    }
}