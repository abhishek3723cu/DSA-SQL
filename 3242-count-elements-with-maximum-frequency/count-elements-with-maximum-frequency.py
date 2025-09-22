from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)                 # Count frequency of each element
        max_freq = max(freq.values())        # Find maximum frequency
        return sum(v for v in freq.values() if v == max_freq)  # Add up all max-freq counts
