class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currMap = {char: False for char in s}

        l, r = 0, 0
        ans = 0 

        currAns = 0
        while l < len(s) and r < len(s):

            if currMap[s[r]]:
                currAns -= 1
                currMap[s[l]] = False
                l += 1

            else:
                currMap[s[r]] = True
                currAns += 1
                r+=1

                ans = max(currAns, ans)


        return ans


