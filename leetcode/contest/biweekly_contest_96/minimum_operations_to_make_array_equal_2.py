from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        diff = [nums2[i] - nums1[i] for i in range(len(nums1))]
        if not any(diff):
            return 0
        if sum(diff) != 0:
            return -1
        if k == 0 and any(diff):
            return -1
        if any(n % k != 0 for n in diff):
            return -1
        return sum(n for n in diff if n > 0) // k


print(Solution().minOperations([4,3,1,4], [1,3,7,1], 3))  # 2
print(Solution().minOperations([3,8,5,2], [2,4,1,6], 1))  # -1
print(Solution().minOperations([4,3,1,4], [1,3,7,1], 0))  # -1
