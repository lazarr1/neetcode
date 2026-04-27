class Solution:

    # 
    def encode(self, strs: List[str]) -> str:

        # technically O(n^2)... new string object is created?
        ans = ""
        for string in strs:
            ans += str(len(string))
            ans += ":"
            ans += string
        
        return ans
        

    def decode(self, s: str) -> List[str]:
        r = 0
        ans = []
        while r < len(s):
            i = r
            curLen = ""

            while s[i] != ":" and i < len(s):
                curLen += s[i]
                i += 1

            i += 1
            print(curLen)
            curLen = int(curLen)
            ans.append(s[i:i+curLen])

            r = i + curLen


        return ans
