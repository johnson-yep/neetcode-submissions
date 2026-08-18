class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS, seenT = {}, {}

        for i in range(len(s)):
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)
        for i in seenS:
            if seenS[i] != seenT.get(i):
                return False

        return True