class Solution:
    def numSteps(self, s: str) -> int:
        s = "0" + s
        arr = list(s)
        ans = 0
        i = len(arr) - 1
        while (i > 1 and arr[i] != 1):
            if arr[i] == '1':
                ans += 1
                arr[i] = '0'
                for j in range(i - 1, -1, -1):
                    if arr[j] == '0':
                        ans += (i - j)
                        arr[j] = '1'
                        i = j 
                        break
                    else:
                        arr[j] = '0'
            else:
                ans += 1
                i -= 1
        return ans