class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x:float,n:int) -> float:
            if n == 0 or abs(n) == 1 or abs(n) == 2:
                return x ** n
            if n % 2 == 0:
                temp = pow(x,n/2)
                return pow(temp,2)
            else:
                temp = pow(x,(n-1)/2)
                return pow(temp,2) * x
        return pow(x,n)
