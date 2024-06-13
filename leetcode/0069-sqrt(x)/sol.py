class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        low = 0
        high = x / 2 
        while low <= high:
            mid = int((high + low) // 2)
            if mid * mid == x or ((mid+1) * (mid+1) > x and mid * mid < x):
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return x