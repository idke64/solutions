class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [[nums[0]]]
            ans = []
            for i in range(len(nums)):
                temp = nums.copy()
                temp.pop(i)

                arr = helper(temp)
                for p in arr:
                    p.append(nums[i])
                    ans.append(p)
            return ans

        return helper(nums)