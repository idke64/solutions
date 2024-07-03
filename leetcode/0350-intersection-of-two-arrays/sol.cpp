class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> freq1;
        for (int i = 0; i < nums1.size(); i++){
            if (!freq1.contains(nums1[i])){
                freq1[nums1[i]] = 0;
            }
            freq1[nums1[i]]++;
        }
        vector<int> ans;
        for (int i = 0; i < nums2.size(); i++){
            if (freq1.contains(nums2[i]) && freq1[nums2[i]] != 0){
                ans.push_back(nums2[i]);
                freq1[nums2[i]]--;
            }
        }
        return ans;
        
    }
};