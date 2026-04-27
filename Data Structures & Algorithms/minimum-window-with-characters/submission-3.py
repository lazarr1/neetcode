class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = {}

        for char in t:
            target[char] = target.get(char, 0) + 1

        sChars = {}
        for char in s:
            sChars[char] = sChars.get(char, 0) + 1
        
        for char in t:
            if sChars.get(char, 0) < target[char]:
                return ""

        l = 0
        currMin = len(s)
        ans = [l, len(s)-1]

        currMap = {}

        def checkContained():
            for char in t:
                if currMap.get(char, 0) < target[char]:
                    return False
            
            return True


        for r in range(len(s)):
            currMap[s[r]] = currMap.get(s[r], 0) + 1

            while checkContained():
                if r - l + 1 <= currMin:
                    currMin = r - l + 1
                    ans = [l, r]
                
                
                currMap[s[l]] -= 1
                l += 1
            





        return s[ans[0]: ans[1]+1]
        

        