from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        i = 0
        while i <= len(digits):
            if i == len(digits):
                digits.append(1)
                break
            else:
                s = digits[i] + 1
                if s > 9:
                    s -= 10
                    digits[i] = s
                    i += 1
                else:
                    digits[i] = s
                    break
        return digits[::-1]


print(Solution().plusOne([9,9,9]))  # [1,0,0,0]
