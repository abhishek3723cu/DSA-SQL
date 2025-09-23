class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split by '.' and convert to integers
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Make lengths equal by padding with 0
        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))
        
        # Compare each revision
        for i in range(max_len):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0
