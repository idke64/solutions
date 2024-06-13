class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        psum = [0]
        m = {
            0 : 1
        }
        for i in range(len(nums)):
            num = (nums[i] + psum[-1]) % k
            psum.append(num)
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        for i in range(len(psum)):
            if m[psum[i]] > 1 and ((i - 1 < 0 or psum[i-1] != psum[i]) and (i + 1 >= len(psum) or psum[i+1] != psum[i])):
                return True
            elif ((i - 1 >= 0 and psum[i-1] == psum[i]) or (i + 1 < len(psum) and psum[i+1] == psum[i])) and m[psum[i]] > 2:
                return True
        return False