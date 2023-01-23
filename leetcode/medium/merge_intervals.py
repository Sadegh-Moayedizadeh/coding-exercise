from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
