class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        import math
        
        def steps_in_range(l, r):
            total = 0
            k = 0
            start = 1
            while start <= r:
                end = start * 4 - 1
                # overlap between [start, end] and [l, r]
                overlap = max(0, min(r, end) - max(l, start) + 1)
                if overlap > 0:
                    total += overlap * (k + 1)
                start *= 4
                k += 1
            return total

        ans = 0
        for l, r in queries:
            total_steps = steps_in_range(l, r)
            ans += (total_steps + 1) // 2  # ceil division
        return ans
