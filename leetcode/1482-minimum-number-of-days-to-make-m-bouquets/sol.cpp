class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int low = 0;
        int high = 0;
        for (int day : bloomDay){
            high = max(day, high);
        }
        while (low <= high){
            int mid = low + (high - low) / 2;
            
            bool solved = solve(mid,bloomDay,m,k);
            if (solved && !solve(mid-1,bloomDay,m,k)){
                return mid;
            }
            if (solved){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return -1;
        
    }
    bool solve(int num, vector<int>& bloomDay, int m, int k) {
        int count = 0;
        int curr_len = 0;
        for (int i = 0; i < bloomDay.size(); i++){
            if (bloomDay[i] <= num){
                curr_len++;
                if (curr_len == k){
                    count++;
                    curr_len = 0;
                }
            }
            else{
                curr_len = 0;
            }
        }
        return count >= m;
    }
};`