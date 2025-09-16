from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # keep merging while top two are non-coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                lcm = a * b // gcd(a, b)
                stack.append(lcm)
        
        return stack
