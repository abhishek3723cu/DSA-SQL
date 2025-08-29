class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_n, even_n = (n + 1) // 2, n // 2
        odd_m, even_m = (m + 1) // 2, m // 2
        return odd_n * even_m + even_n * odd_m
