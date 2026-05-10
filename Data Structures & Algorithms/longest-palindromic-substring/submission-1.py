class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0] * len(s)
        resLen = [0] *len(s)
        maxi = 0
        ans = ''

        for i in range(len(s)):
            l = i
            r = l
            while l >= 0 and r < len(s):
                substr = s[l:r+1] if (l != r) else s[l]
                
                if len(substr) > maxi:
                    maxi = len(substr)
                    ans = substr

                if l -1 >= 0 and r +1  < len(s) and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                else:
                    break
            
            if i > 0 and s[i] == s[i-1]:
                l = i - 1
                r = l + 1
                while l >= 0 and r < len(s):
                    substr = s[l:r+1]
                    if len(substr) > maxi:
                        maxi = len(substr)
                        ans = substr

                    if l -1 >= 0 and r +1  < len(s) and s[l-1] == s[r+1]:
                        l -= 1
                        r += 1
                    else: 
                        break
                    
        return ans