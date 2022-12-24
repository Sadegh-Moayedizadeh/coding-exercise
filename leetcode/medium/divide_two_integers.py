class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = dividend // divisor
        if quotient < 0 and dividend % divisor != 0:
            quotient += 1
        if quotient > 2**31 - 1:
            return 2**31 - 1
        if quotient < -2**31:
            return -2**31
        return quotient
