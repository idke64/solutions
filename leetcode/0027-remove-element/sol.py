class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == val:
                while last >= 0 and nums[last] == val:
                    last -= 1
                if last <= i:
                    break
                temp = nums[last]
                nums[last] = val
                nums[i] = temp
        return last + 1