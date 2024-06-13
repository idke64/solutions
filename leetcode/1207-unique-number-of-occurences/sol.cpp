class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> map;
        for (auto it : arr){
            map[it]++;
        }
        set<int> set;
        for (auto p : map){
            if (set.contains(p.second)){
                return false;
            }
            set.insert(p.second);
        }
        return true;
    }
};