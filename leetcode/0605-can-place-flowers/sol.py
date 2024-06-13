class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        temp_total = 0
        if flowerbed[0] == 0:
            temp_total = 2
        total = 0
        for i in range(1, len(flowerbed)):
            if (flowerbed[i] == 0 and flowerbed[i-1] == 1) or (flowerbed[i] == 0 and temp_total > 0):
                temp_total += 1
            if flowerbed[i] == 1 and flowerbed[i-1] == 0:
                total += (temp_total+1) // 2 - 1
                temp_total = 0
        total += (temp_total + 2) // 2 - 1
        return total >= n
