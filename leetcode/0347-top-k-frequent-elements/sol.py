class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 0
            m[nums[i]] += 1
        freq = []
        for key in m:
            freq.append((m[key],key))
        freq.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(freq[i][1])
        return ans