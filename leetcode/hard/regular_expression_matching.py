class Solution(object):
    def isMatch(self, s, p):
        cache = {}
        def dp(s_index, p_index):
            if (s_index, p_index) not in cache:
                if p_index == len(p):
                    ans = s_index == len(s)
                else:
                    first_match = \
                        s_index < len(s) and p[p_index] in {s[s_index], '.'}
                    if p_index+1 < len(p) and p[p_index+1] == '*':
                        ans = \
                            dp(s_index, p_index+2) or \
                                first_match and dp(s_index+1, p_index)
                    else:
                        ans = first_match and dp(s_index+1, p_index+1)

                cache[s_index, p_index] = ans
            return cache[s_index, p_index]

        return dp(0, 0)


print(Solution().isMatch('aaa', 'aaa'))  # True
print(Solution().isMatch('aaa', 'aa'))  # False
print(Solution().isMatch('aaa', '...'))  # True
print(Solution().isMatch('aaa', '..'))  # False
print(Solution().isMatch('aaa', 'a*'))  # True
print(Solution().isMatch('aaa', '.*'))  # True
print(Solution().isMatch('aab', 'c*a*b*'))  # True
print(Solution().isMatch('ab', '.*c'))  # False
print(Solution().isMatch('aaa', 'aaaa'))  # False
print(Solution().isMatch('aaa', 'a*a'))  # True
print(Solution().isMatch('aaa', 'ab*a*c*a'))  # True
