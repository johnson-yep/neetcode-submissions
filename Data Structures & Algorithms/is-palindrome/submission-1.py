class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedS = re.sub(r"[^A-Za-z0-9]", "", s).lower()

        n = len(processedS)
        l, r = 0, n-1
        while l<r:
            if processedS[l]!=processedS[r]:
                return False
            l+=1
            r-=1

        return True
