class Solution:
    _integer_to_roman_symbol = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def intToRoman(self, num: int) -> str:
        result_list = []
        for base_number in \
                sorted(self._integer_to_roman_symbol.keys(), reverse=True):
            while num >= base_number:
                result_list.append(self._integer_to_roman_symbol[base_number])
                num -= base_number
            if num <= 0:
                break
        return ''.join(result_list)


print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
