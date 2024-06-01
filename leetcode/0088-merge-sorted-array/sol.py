class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        queue = nums1[:m]
        for i in range(len(nums1)):
            if not queue:
                nums1[i] = nums2[j]
                j += 1
                continue
            if j == n:
                nums1[i] = queue.pop(0)
                continue
            if queue[0] < nums2[j]:
                nums1[i] = queue[0]
                queue.pop(0)
            else:
                nums1[i] = nums2[j]
                j += 1
        