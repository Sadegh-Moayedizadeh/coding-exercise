class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = -1 * int(str(abs(x))[::-1])
        else:
            result = int(str(x)[::-1])
        if not -2**31 <= result <= 2**31-1:
            return 0
        return result
