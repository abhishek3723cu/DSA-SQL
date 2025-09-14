from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(word: str) -> str:
            return ''.join('*' if c in vowels else c for c in word.lower())
        
        # Preprocessing
        exact_set = set(wordlist)
        case_map = {}
        vowel_map = {}
        
        for word in wordlist:
            lower = word.lower()
            case_map.setdefault(lower, word)   # keep first match
            vowel_map.setdefault(devowel(lower), word)
        
        # Answer queries
        result = []
        for q in queries:
            if q in exact_set:
                result.append(q)   # exact match
            elif q.lower() in case_map:
                result.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:
                result.append(vowel_map[devowel(q)])
            else:
                result.append("")
        
        return result
