class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> ans1;
        set<int> ans2;
        for (int i = 0; i < nums1.size(); i++){
            ans1.insert(nums1[i]);
        }
        for (int i = 0; i < nums2.size(); i++){
            ans2.insert(nums2[i]);
        }
        for (int i = 0; i < nums1.size(); i++){
            ans2.erase(nums1[i]);
        }
        for (int i = 0; i < nums2.size(); i++){
            ans1.erase(nums2[i]);
        }
        vector<vector<int>> v;
        vector<int> v1(ans1.begin(), ans1.end());
        vector<int> v2(ans2.begin(), ans2.end());
        v.push_back(v1);
        v.push_back(v2);
        return v;
    }
};