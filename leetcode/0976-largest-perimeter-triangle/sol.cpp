class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end(), greater<int>());
        int s1 = 1;
        int s2 = 2;
        int s3 = 0;
        while (s1 != nums.size() - 1 && s2 != nums.size()){
            while (s3 < s1){
                if (nums[s1] + nums[s2] > nums[s3]){
                    return nums[s1] + nums[s2] + nums[s3];
                }
                s3++;
            }
            if (s1 == s2 - 1){
                s2++;
            }
            else{
                s1++;
            }
        }
        return 0;
    }
};