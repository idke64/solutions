class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        queue<int> queue;
        string ans = "";
        int shortest = s.length() + 1;
        s += "1";
        for (int i = 0; i < s.length(); i++){
            if (s[i] == '1'){
                if (queue.size() >= k){
                    int len = queue.back() - queue.front() + 1;
                    if (len <= shortest){
                        string temp_ans = s.substr(queue.front(),queue.back() - queue.front() + 1);
                        if (temp_ans.compare(ans) < 0 || len < shortest){
                            ans = temp_ans;
                        }
                        shortest = len;
                    }
                    queue.pop();
                }
                queue.push(i);
            }
        }
        return ans;
    }
};