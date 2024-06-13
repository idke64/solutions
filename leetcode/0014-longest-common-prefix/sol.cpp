class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string lcp = strs[0];
        for (auto str : strs){
            string temp = "";
            for (int i = 0; i < lcp.length(); i++){
                if (lcp[i] != str[i]){
                    break;    
                }
                temp += lcp[i];
            }
            lcp = temp;
        }
        return lcp;
    }
};