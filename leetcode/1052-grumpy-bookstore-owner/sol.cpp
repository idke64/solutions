class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        vector<int> psum;
        psum.push_back(0);
        int sum = 0;
        int sum2 = 0;
        for (int i = 0; i < customers.size(); i++){
            if (i < minutes){
                sum += customers[i];
            }
            else{
                sum2 += customers[i] * (grumpy[i] ^ 1);
            }
        }
        int ans = sum + sum2;
        for (int i = minutes; i < customers.size(); i++){
            sum += customers[i] - customers[i-minutes];
            sum2 += customers[i - minutes] * (grumpy[i - minutes] ^ 1) - customers[i] * (grumpy[i] ^ 1);
            ans = max(ans,sum + sum2);
        }
        return ans;
    }
};