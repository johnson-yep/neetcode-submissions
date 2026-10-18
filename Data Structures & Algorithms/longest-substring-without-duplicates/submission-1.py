class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        n = len(s)
        seen = {}
        best = 0
        for r in range(n):
            
            if s[r] in seen and seen[s[r]]>=l:
                l = seen[s[r]]
            seen[s[r]] = r

            best = max(best, r-l)
            
        return best
