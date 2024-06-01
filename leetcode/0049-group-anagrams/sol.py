class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        ans = []
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in s:
                ans[s[sorted_str]].append(strs[i])
            else:
                ans.append([strs[i]])
                s[sorted_str] = len(ans) - 1
        return ans