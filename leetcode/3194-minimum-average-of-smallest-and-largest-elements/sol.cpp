class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        double ans = 51;
        for(int i = 0; i < nums.size() / 2; i++){
            ans = min(ans,(double)(nums[nums.size() - 1 - i] + nums[i]) / 2);
        }
        return ans;
    }
};