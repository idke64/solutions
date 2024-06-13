class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        highest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= highest:
                ans.append(True)
            else:
                ans.append(False)
        return ans