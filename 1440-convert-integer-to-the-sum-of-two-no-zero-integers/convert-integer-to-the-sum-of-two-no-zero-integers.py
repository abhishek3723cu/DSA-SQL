class Solution:
    def getNoZeroIntegers(self, n: int) -> [int]:
        def no_zero(x):
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if no_zero(a) and no_zero(b):
                return [a, b]
