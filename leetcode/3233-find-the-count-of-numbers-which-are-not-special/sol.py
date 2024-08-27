class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(x):
            if x == 1:
                return False
            for i in range(2,int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True


        special = 0
        i = math.ceil(math.sqrt(l))
        while i * i <= r:
            if is_prime(i):
                special += 1
            i += 1
        return r - l + 1 - special
            
            