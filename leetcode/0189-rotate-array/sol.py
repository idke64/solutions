class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_copy = nums.copy()
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = n_copy[i]
