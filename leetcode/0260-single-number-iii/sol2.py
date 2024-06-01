class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        right_most_bit = xor & -xor
        a = 0
        b = 0
        for i in range(len(nums)):
            if nums[i] & right_most_bit:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a,b]

        