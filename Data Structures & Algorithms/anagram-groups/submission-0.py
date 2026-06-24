class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramKey = {}
        result = []
        for word in strs:
            key = ''.join(sorted(word))
            anagramKey[key] = anagramKey.get(key,0) +1

        for key in anagramKey:
            currAnagram = []
            for word in strs:
                if ''.join(sorted(word)) == key:
                    currAnagram.append(word)
            result.append(currAnagram)
        return result