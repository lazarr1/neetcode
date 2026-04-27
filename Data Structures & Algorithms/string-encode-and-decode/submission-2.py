class Solution:

    # 
    def encode(self, strs: List[str]) -> str:
        ret = ""

        for string in strs:
            ret += '"'
            for char in string:
                if char == '"':
                    ret += "\\\""
                elif char == "\\":
                    ret += "\\a"
                else:
                    ret += char
            ret += '"'
        
        # ret = ret[:len(ret) - 1]

        return ret

    def decode(self, s: str) -> List[str]:
        ans = []

        r = 1
        decoded_str = ""

        while r < len(s):
            char = s[r]


            if char == '"' and s[r - 1] != '\\':
                ans.append(decoded_str)
                decoded_str = ""
                r += 1
            elif char == "a" and s[r - 1] == "\\":
                r+=1
                continue
            elif char == '"' and s[r - 1] == '\\':
                decoded_str = decoded_str[:-1] + char
            else:
                decoded_str += char 

            r += 1


        return ans
