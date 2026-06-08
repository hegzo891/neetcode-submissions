class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        lengths = len(s)
        lengthr = len(t)
        while l < lengths and r < lengthr:
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        return  l == lengths 
