class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if (x < 0):
            neg = True
            x *= -1
        
        s = list(str(x))
        for i in range(int(len(s) / 2)):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
        ans = 0
        if (neg):
            ans = int("-" + ''.join(s))
        else:
            ans = int(''.join(s))
        if ans < 2 ** 31 - 1 and ans > -2 ** 31 - 1:
            return ans
        else:
            return 0
            
        