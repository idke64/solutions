class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(),position.end());
        int low = 1;
        int high = position.back() - position.front();
        while (low <= high){
            int mid = low + (high - low) / 2;
            bool solved = solve(mid,position,m);
            if (solved && !solve(mid + 1,position,m)){
                return mid;
            }
            if (solved){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return 1;
    }
    bool solve(int num, vector<int>& position, int m){
        int prev = 0;
        int count = 1;
        for (int i = 1; i < position.size(); i++){
            if (position[i] - position[prev] >= num){
                count++;
                prev = i;
            }
        }
        //5 3 3 2
        //t t t f
        return count >= m;
    }
};