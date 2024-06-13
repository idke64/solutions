class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        def binary_search(i: int) -> int:
            high = len(intervals) - 1
            low = 0
            while low <= high:
                mid = low + (high - low) // 2
                if i == mid:
                    high = mid - 1
                    continue
                if intervals[i][0] >= intervals[mid][0] and intervals[i][0] <= intervals[mid][1]:
                    return mid
                if intervals[i][0] < intervals[mid][0]:
                    high = mid - 1
                if intervals[i][0] > intervals[mid][0]:
                    low = mid + 1
            return -1
        i = 0
        while i < len(intervals):
            ind = binary_search(i)
            if ind != -1:
                intervals[ind][1] = max(intervals[ind][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals