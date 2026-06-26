class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        teen = {}
        
        for c in s:
            seen[c] = seen.get(c,0) + 1
        for c in t:
            if c in seen:
                teen[c] = teen.get(c,0) + 1
            else:
                return False
        for key in seen:
            if seen[key] == teen[key]:
                continue
            else:
                return False

        return True