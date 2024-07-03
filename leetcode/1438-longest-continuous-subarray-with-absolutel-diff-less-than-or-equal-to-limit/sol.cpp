class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        map<int,int> map;
        int start = 0;
        int ans = 0;
        for (int i = 0; i < nums.size(); i++){
            if (!map.contains(nums[i])){
                map[nums[i]] = 0;
            }
            map[nums[i]]++;
            int first = map.begin()->first;
            int last = map.rbegin()->first;
            if (last - first > limit){
                for (int j = start; j < i; j++){
                    map[nums[j]]--;
                    if (map[nums[j]] == 0){
                        map.erase(nums[j]);
                    }
                    int first2 = map.begin()->first;
                    int last2 = map.rbegin()->first;
                    if (last2 - first2 <= limit){
                        start = j + 1;
                        break;
                    } 
                }
            }
            ans = max(ans, i - start + 1);
        }
        return ans;
    }
};