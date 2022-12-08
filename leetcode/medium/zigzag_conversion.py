from itertools import chain


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        nested_list = []
        for i in range(numRows):
            nested_list.append(self._extract_row(
                row_number=i,
                numRows=numRows,
                s=s
                )
            )
        return ''.join(chain.from_iterable(nested_list))

    def _extract_row(self, row_number: int, numRows: int, s: str):
        characters_in_middle = numRows - 2
        result = []
        return [
            s[i]
            for i in range(len(s))
            if (
                i % (characters_in_middle + numRows) == (row_number)
                or i % (characters_in_middle + numRows) ==
                (characters_in_middle + numRows) - (row_number)
            )
        ]
        return result
