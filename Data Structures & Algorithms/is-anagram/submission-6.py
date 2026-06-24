class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = dict()
        teen = dict()
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            if char in seen:
                teen[char] = teen.get(char, 0) + 1
                continue 
            else:
                return False
        for key in seen:
            if seen.get(key) == teen.get(key):
                continue
            else:
                return False
        return True