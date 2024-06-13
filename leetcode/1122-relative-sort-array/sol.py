class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {}
        for i in range(len(arr2)):
            m[arr2[i]] = 0
        ans1 = []
        for i in range(len(arr1)):
            if arr1[i] in m:
                m[arr1[i]] += 1
            else:
                ans1.append(arr1[i])
        ans2 = []
        print(m)
        for key in m:
            for i in range(m[key]):
                ans2.append(key)
        return ans2 + sorted(ans1)