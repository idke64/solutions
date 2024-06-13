class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        count = 0
        for i in range(len(s)):
            if s[i] in chars:
                chars.remove(s[i])
                count += 1
            else:
                chars.add(s[i])
        return (count * 2) + (len(chars) > 0)