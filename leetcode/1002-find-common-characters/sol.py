class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alp = [0 for _ in range(26)]
        for i in range(len(words[0])):
            alp[ord(words[0][i]) - 97] += 1
        for i in range(1,len(words)):
            alp2 = [0 for _ in range(26)]
            for j in range(len(words[i])):
                alp2[ord(words[i][j]) - 97] += 1
            for j in range(26):
                alp[j] = min(alp[j],alp2[j])
        ans = ""
        for i in range(26):
            ans += chr(i + 97) * alp[i]
                
        return ans