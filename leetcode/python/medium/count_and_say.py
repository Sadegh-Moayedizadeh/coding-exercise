class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self._say(int(self.countAndSay(n - 1)))

    def _say(self, n: int) -> str:
        result_list = []
        n = str(n)
        current_digit = n[0]
        count = 1
        for digit in n[1:]:
            if digit == current_digit:
                count += 1
            else:
                result_list.append(str(count) + current_digit)
                count = 1
                current_digit = digit
        else:
            result_list.append(str(count) + current_digit)
        return ''.join(result_list)


print(Solution().countAndSay(4))
