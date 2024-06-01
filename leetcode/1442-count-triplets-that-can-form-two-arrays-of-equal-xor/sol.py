class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            curr = arr[i]
            for j in range(i+1, len(arr)):
                curr ^= arr[j]
                if curr == 0: 
                    ans += j - i
        return ans