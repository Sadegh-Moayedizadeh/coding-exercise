from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for string in strs:
            result_dict[''.join(sorted(string))].append(string)
        return list(result_dict.values())


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
