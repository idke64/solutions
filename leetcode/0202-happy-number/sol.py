class Solution:
    def isHappy(self, n: int) -> bool:
        m = set()
        def sum_square(n: int) -> int:
            digits = int(math.log(n, 10)) + 1
            sum = 0
            for i in range(1, digits + 1):
                num = (n % (10 ** i)) // 10 ** (i-1)
                sum += num * num
            return sum
        while n != 1:
            if n in m:
                return False
            m.add(n)
            n = sum_square(n)
        return True
            
