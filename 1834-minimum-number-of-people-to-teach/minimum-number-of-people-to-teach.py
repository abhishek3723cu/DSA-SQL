class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert each user's languages to a set
        langs = [set(l) for l in languages]
        
        # Step 1: find all users in "bad" friendships
        bad_users = set()
        for u, v in friendships:
            if langs[u-1].isdisjoint(langs[v-1]):  # no common language
                bad_users.add(u-1)
                bad_users.add(v-1)
        
        # Step 2: check each language
        res = float('inf')
        for lang in range(1, n+1):
            count = 0
            for user in bad_users:
                if lang not in langs[user]:
                    count += 1
            res = min(res, count)
        
        return 0 if res == float('inf') else res
