class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        visited = set()
        ans = 0
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            temp_ans = 0
            j = 0
            while nums[i] + j in s:
                visited.add(nums[i] + j)
                j += 1
                temp_ans += 1
            j = 1
            while nums[i] - j in s:
                visited.add(nums[i] - j)
                j += 1
                temp_ans += 1
            
            ans = max(temp_ans, ans)
        return ans

        