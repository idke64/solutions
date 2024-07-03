class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int ans = 0;
        vector<int> v;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] % 2 != 0){
                v.push_back(i);
            }
        }
        if (k > v.size()){
            return 0;
        }
        for (int i = 0; i < v.size() - k + 1; i++){
            int left_ind = i;
            int right_ind = i + k - 1;
            int left2 = 0;
            int right2 = nums.size() - 1;
            if (left_ind - 1 >= 0){
                left2 = v[left_ind - 1] + 1;
            }
            if (right_ind + 1 < v.size()){
                right2 = v[right_ind + 1] - 1;
            }
            ans += 1 + (v[left_ind] - left2) + (right2 - v[right_ind]) + ((v[left_ind] - left2) * (right2 - v[right_ind]));
        }

        return ans;
    }
};