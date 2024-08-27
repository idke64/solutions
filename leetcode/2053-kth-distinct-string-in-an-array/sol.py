class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        occ = {}
        for i in range(len(arr)):
            if arr[i] not in occ:
                occ[arr[i]] = 0
            occ[arr[i]] += 1
        curr = 1
        for i in range(len(arr)):
            if occ[arr[i]] == 1:
                if curr == k:
                    return arr[i]
                curr += 1
        return ""