class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        oBrace = {"[": 1, "(": 2, "{": 3}
        cBrace = {"]": 1, ")": 2, "}": 3}
        stack = []
        for brace in s:
            if brace in oBrace:
                stack.append(brace)
            if brace in cBrace:
                if not stack or not oBrace[stack.pop()] == cBrace[brace]:
                    return False
        if not stack:
            return True
        else:
            return False