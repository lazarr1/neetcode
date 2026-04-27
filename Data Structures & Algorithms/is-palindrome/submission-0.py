class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        alphaNum = "abcdefghijklmnopqrstuvwxyz0123456789"

        while l < r:
            if s[l] not in alphaNum:
                l+=1
                continue
            if s[r] not in alphaNum:
                r-=1
                continue

            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True
