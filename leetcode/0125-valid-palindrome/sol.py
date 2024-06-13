class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left <= right):
            if not s[left].isalnum() or not s[right].isalnum():
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
            
