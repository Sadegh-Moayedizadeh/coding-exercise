from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for word in strs[1:]:
            i = 0
            for i in range(len(result)):
                if i == len(word) or result[i] != word[i]:
                    break
                i += 1
            result = result[: i]
        return result


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
