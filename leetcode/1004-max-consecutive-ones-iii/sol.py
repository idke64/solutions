class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                arr.append(i)
        if k >= len(arr):
            return len(nums)

        ans = 0
        left = 0
        for i in range(k - 1, len(arr)):
            if i == len(arr) - 1:
                ans = max(len(nums) - left,ans)
                break
            ans = max(arr[i + 1] - left,ans)
            if arr[i - (k - 1)] - 1 >= 0 and nums[arr[i - (k - 1)] - 1] == 1:
                left = arr[i - (k - 1)] + 1
            else:
                left += 1
        return ans