class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        longest = 0
        start = 0
        for i in range(len(t)):
            found = False
            for j in range(start,len(s)):
                if s[j] == t[i]:
                    found = True
                    start = j + 1
                    break
            if not found:
                break
            else:
                longest += 1
        return len(t) - longest