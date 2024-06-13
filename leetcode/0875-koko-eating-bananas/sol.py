class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        def check(num: int) -> int:
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / num)
            return total
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 1:
                t = check(mid)
                if t > h:
                    low = mid + 1
                    continue
                else:
                    return 1
            t1 = check(mid)
            t2 = check(mid-1)
            if t2 > h and t1 <= h:
                return mid
            if t1 > h:
                low = mid + 1
            else:
                high = mid - 1