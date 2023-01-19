class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n < 0:
            negative = True
            n = -1 * n
        result = 1
        curr = x
        for dig in bin(n)[2:][::-1]:
            if dig == '1':
                result *= curr
            curr *= curr
        return result if not negative else 1 / result

print(Solution().myPow(2, 10))  # 1024
