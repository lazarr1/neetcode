class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        lut = {}

        for char in s:
            lut[char] = lut.get(char, 0) + 1

        for char in t:
            if char not in lut:
                return False
            
            lut[char] -= 1
            if (lut[char] == 0):
                lut.pop(char)
            
        return len(lut) == 0