class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_sort = [0 for _ in range(3)]
        for i in range(len(nums)):
            count_sort[nums[i]] += 1
        start = 0
        for i in range(3):
            for j in range(start, count_sort[i] + start):   
                nums[j] = i
            start += count_sort[i]