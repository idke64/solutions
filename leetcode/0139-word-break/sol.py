class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = set(wordDict)
        visited = [False] * len(s)
        ans = [False]
        def solve(start: int):
            if start == len(s):
                ans[0] = True
                return
            if visited[start]:
                return
            visited[start] = True
            curr_word = ""
            for i in range(start, len(s)):
                curr_word += s[i]
                if curr_word in dict:
                    solve(i + 1)
        solve(0)
        return ans[0]