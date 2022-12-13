class Solution:
    def myAtoi(self, s: str) -> int:        
        digits = []
        s = s.lstrip(' ')
        sign = 1
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]
        for char in s:
            if not char.isdigit():
                break
            digits.append(char)

        if not digits:
            return 0

        number = int(''.join(digits))
        if sign == -1 and number > 2**31:
            return -2**31
        elif sign == 1 and number > 2**31 - 1:
            return 2**31-1
        return sign * int(''.join(digits))


print(Solution().myAtoi(' ++42'))
print(Solution().myAtoi('    -42'))
