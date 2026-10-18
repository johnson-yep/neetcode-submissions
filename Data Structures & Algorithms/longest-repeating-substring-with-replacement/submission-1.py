class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        l = best = 0

        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]] +=1
            else:
                seen[s[r]] = 1
            
            while (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -=1
                l+=1
            
            best = max(best, r-l+1)

        return best