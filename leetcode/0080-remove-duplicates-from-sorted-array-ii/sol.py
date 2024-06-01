class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        s = set()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] and nums[i] not in s:
                s.add(nums[i])
                nums[k] = nums[i]
                k += 1
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k