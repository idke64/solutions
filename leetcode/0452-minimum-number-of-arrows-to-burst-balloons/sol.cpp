class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int count = points.size();
        sort(points.begin(),
          points.end(),
          [] (const vector<int> &a, const vector<int> &b)
          {
              return a[0] < b[0];
          });
        for (int i = 1; i < points.size(); i++){
            if (points[i-1][1] >= points[i][0]){
                count--;
                points[i][1] = min(points[i-1][1],points[i][1]);
            }
        }
        return count;
    }
};