import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        left = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if i == (n // i):
                    factors.insert(left,i)
                else:
                    factors.insert(left,i)
                    factors.insert(left+1,n // i)
                left += 1
        print(factors)
        if k > len(factors):
            return -1
        return factors[k-1] 
