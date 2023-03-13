class Solution(object):
    _roman_symbol_to_integer_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0
        while index < len(s) - 1:
            if self._roman_symbol_to_integer_value[s[index]] < \
                    self._roman_symbol_to_integer_value[s[index + 1]]:
                result -= self._roman_symbol_to_integer_value[s[index]]
            else:
                result += self._roman_symbol_to_integer_value[s[index]]
            index += 1
        result += self._roman_symbol_to_integer_value[s[index]]
        return result


print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))
