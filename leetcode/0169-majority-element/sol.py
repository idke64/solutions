class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        max_occ = 0
        mode = 0
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
            else:
                m[nums[i]] += 1
            if m[nums[i]] > max_occ:
                max_occ = m[nums[i]]
                mode = nums[i]
        return mode
        