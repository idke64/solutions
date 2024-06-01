class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        sum = 0
        left = 0
        for i in range(len(s)):
            diff = abs(ord(s[i]) - ord(t[i]))
            if diff > maxCost:
                sum = 0
                left = i + 1
                continue
            sum += diff
            if sum > maxCost:
                for j in range(left, i):
                    sum -= abs(ord(s[j]) - ord(t[j]))
                    if sum <= maxCost:
                        left = j + 1
                        break
            max_length = max(max_length, i - left + 1)
            
        return max_length
        