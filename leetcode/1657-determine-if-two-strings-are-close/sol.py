class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s = set(word1)
        for c in word2:
            if c not in s:
                return False
        for c in word2:
            if c in s:
                s.remove(c)
        if len(s) != 0:
            return False
        
        w1_frq = [0 for _ in range(26)]
        w2_frq = [0 for _ in range(26)]
        for i in range(len(word1)):
            w1_frq[ord(word1[i]) - 97] += 1
            w2_frq[ord(word2[i]) - 97] += 1
        w1_frq.sort()
        w2_frq.sort()
        for i in range(26):
            if w1_frq[i] != w2_frq[i]:
                return False
        return True