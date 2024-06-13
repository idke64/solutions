class Solution:
    def maxDepth(self, s: str) -> int:
        opened = 0
        nd = 0
        for i in range(len(s)):
            if s[i] == "(":
                opened += 1
            if s[i] == ")":
                opened -= 1
            nd = max(nd, opened)
        return nd