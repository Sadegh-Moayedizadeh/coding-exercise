from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                intervals.append(newInterval)
            elif newInterval[0] >= intervals[i][0] and \
                    newInterval[0] <= intervals[i + 1][0]:
                intervals.insert(i + 1, newInterval)
                break
        if not intervals:
            intervals = [newInterval]
        return self._merge(intervals)

    def _merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last = result.pop()
                if interval[0] <= last[1]:
                    result.append(
                        [min(interval[0], last[0]), max(interval[1], last[1])]
                    )
                else:
                    result.append(last)
                    result.append(interval)
        return result


print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
