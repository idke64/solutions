class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        queue<int> queue;
        int ans = 0;
        for (int i = 0; i < nums.size(); i++){
            if (queue.front() == i - k){
                queue.pop();
            }
            int curr = nums[i] ^ (queue.size() % 2);
            if (curr == 0 && i > nums.size() - k){
                return -1;
                break;
            }
            if (curr == 0){
                ans++;
                queue.push(i);
            }
            
        }
        return ans;
    }
};