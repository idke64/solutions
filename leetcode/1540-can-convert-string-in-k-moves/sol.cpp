class Solution {
public:
    bool canConvertString(string s, string t, int k) {
        if (s.length() != t.length()){
            return false;
        }
        map<int,int> used;
        for (int i = 0; i < s.length(); i++){
            int dist = (int(t[i]) - int(s[i]));
            if (dist < 0){
                dist += 26;
            }
            if (dist == 0){
                continue;
            }
            if (dist <= k){
                if (!used.contains(dist)){
                    used[dist] = 0;
                }
                used[dist]++;
            }
            else{
                return false;
            }
        }
        for (auto x : used){
            if (x.first + (26 * (x.second - 1)) > k){
                return false;
            }
        }
        return true;
    }
};