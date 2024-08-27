class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        for i in range(len(nums)):
            if target - nums[i] in s:
                for j in range(i):
                    if nums[j] == target - nums[i]:
                        return [i,j]
            s.add(nums[i])