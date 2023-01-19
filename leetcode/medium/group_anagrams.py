from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for i in range(len(strs)):
            if any(i in group for group in result):
                continue
            new_group = set()
            new_group.add(i)
            for j in range(i + 1, len(strs)):
                if any(j in group for group in result):
                    continue
                if Counter(strs[i]) == Counter(strs[j]):
                    new_group.add(j)
            result.append(new_group)
        return list(map(
            list,
            (map(lambda i: strs[i], group) for group in result)
        ))


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
