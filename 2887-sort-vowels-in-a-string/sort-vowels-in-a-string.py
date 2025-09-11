class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU")
        # collect vowels in original order
        vowels = [ch for ch in s if ch in vowels_set]
        # sort by ASCII value (default ord order)
        vowels.sort(key=ord)
        it = iter(vowels)
        # rebuild string: replace vowel positions with sorted vowels, keep others
        return ''.join(next(it) if ch in vowels_set else ch for ch in s)
