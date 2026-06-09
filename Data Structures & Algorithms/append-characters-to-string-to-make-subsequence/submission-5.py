class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        w1, w2 =0, 0
        while w1 < len(s):
            if w2 < len(t) and s[w1] == t[w2]:
                w2 += 1 
            w1 += 1
        
        return len(t) - w2