class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        print(nums)
        x = 1
        for i in range(0, len(nums)):
            if i == len(nums) - 1 and nums[i] >= x:
                return x
            if nums[i] >= x and nums[i+1] < x:
                return x
            else:
                x += 1
        return -1
            
        