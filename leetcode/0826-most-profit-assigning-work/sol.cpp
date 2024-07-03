class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int,int>> jobs;
        for (int i = 0; i < profit.size(); i++){
            jobs.push_back(make_pair(difficulty[i],profit[i]));
        }
        sort(jobs.begin(),jobs.end());
        sort(worker.begin(),worker.end());
        int j = 0;
        priority_queue<int> pq;
        int ans = 0;
        for (int i = 0; i < worker.size(); i++){
            while (j < profit.size() && jobs[j].first <= worker[i]){
                pq.push(jobs[j].second);
                j++;
            }
            if (!pq.empty()){
                ans += pq.top();
            }
        }
        
        return ans;
        
    }
};