class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                if i == len(needle) - 1:
                    return j - i
                i += 1
            else:
                j -= i
                i = 0
            j += 1
        return -1


print(Solution().strStr('sadbutsad', 'sad'))
print(Solution().strStr('leetcode', 'leeto'))
print(Solution().strStr('mississippi', 'issip'))
