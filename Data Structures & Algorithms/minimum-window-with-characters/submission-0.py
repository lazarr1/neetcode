
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        cache = {}
        # freq chart of t:
        freqs = {}
        for char in t:
            freqs[char] = freqs.get(char, 0) + 1


        def dfs(Si, s, currStr, currFreqs):

            if Si == len(s):
                return ''
            char = s[Si]
            if char in currFreqs:
                currFreqs[char] -= 1
                if currFreqs[char] == 0:
                    del currFreqs[char]
                
                if not currFreqs:
                    return currStr + char
            
            currStr += char
            Si += 1
            res1 = dfs(Si, s, currStr, currFreqs)
            res2 = dfs(Si, s, '', freqs.copy())

            if len(res2) <= len(res1) and res2 != '':
                return res2
            return res1
        
        return dfs(0, s, '', freqs.copy())