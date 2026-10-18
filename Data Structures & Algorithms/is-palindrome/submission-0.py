class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        n = len(newS)
        mid = n // 2
        l = r = mid
        if n % 2 == 0:
            l = mid-1
        while l>=0:
            if newS[l] != newS[r]:
                return False
            l-=1
            r+=1

        return True