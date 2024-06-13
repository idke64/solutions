class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
            if (arr[i] * 2 in s and arr[i] != 0) or (arr[i] == 0 and zero_count > 1):
                return True
        return False