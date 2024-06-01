class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for _ in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        total = candy[len(candy) - 1]
        for i in range(len(ratings) - 2, -1, -1):
            if (ratings[i] > ratings[i+1]):
                candy[i] = max(candy[i+1] + 1, candy[i])
            total += candy[i]
        
        return total
            
             

