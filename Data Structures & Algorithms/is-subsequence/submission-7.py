class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                pos = t.find(s[i])
                t = t[pos + 1:]
            else:
                return False
        return True
