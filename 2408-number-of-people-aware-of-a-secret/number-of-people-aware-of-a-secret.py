class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # Day 1: one person knows
        
        for i in range(1, n + 1):
            for j in range(i + delay, min(n, i + forget - 1) + 1):
                dp[j] = (dp[j] + dp[i]) % MOD
        
        # Count people who still remember at day n
        ans = sum(dp[n - forget + 1 : n + 1]) % MOD
        return ans
