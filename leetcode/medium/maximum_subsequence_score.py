from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lst = sorted(zip(nums2, nums1), reverse=True)

        res = 0
        s = lst[0][1]
        m = lst[0][0]
        length = 1

        if length == k:
            res = max(res, s * m)

        heap = []
        heapq.heappush(heap, s)

        for index in range(1, len(lst)):
            m = lst[index][0]
            s += lst[index][1]

            heapq.heappush(heap, lst[index][1])
            length += 1

            if length > k:
                s -= heapq.heappop(heap)
                length -= 1

            if length == k:
                res = max(res, s*m)

        return res


print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))  # 12
print(Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 1))  # 30
