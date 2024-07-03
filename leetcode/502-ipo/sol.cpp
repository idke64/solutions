class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        vector<pair<int,int>> projects;
        for (int i = 0; i < profits.size(); i++){
            projects.push_back(make_pair(capital[i],profits[i]));
        }
        sort(projects.begin(),projects.end());
        priority_queue<int> pq;
        int count = 0;
        for (int i = 0; i < projects.size(); ++i){
            while(w < projects[i].first && count < k && !pq.empty()){
                int profit = pq.top();
                w += profit;
                count++;
                pq.pop();
            }
            if (w >= projects[i].first){
                pq.push(projects[i].second);
            }
            
        }
        while (count < k && !pq.empty()){
            w += pq.top();
            pq.pop();
            count++;
        }
        return w;
    }
};