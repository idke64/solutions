class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        if curr == len(s):
            return True
        for i in range(len(t)):
            if t[i] == s[curr]:
                curr += 1
            if curr == len(s):
                return True
        return False