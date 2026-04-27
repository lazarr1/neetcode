class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        charCounts = {}

        for i in range(len(s)):
            charCounts[s[i]] = charCounts.get(s[i], 0) + 1
            charCounts[t[i]] = charCounts.get(t[i], 0) - 1

            if (charCounts[t[i]] == 0):
                charCounts.pop(t[i])
            
            if (s[i] in charCounts):
                if (charCounts[s[i]] == 0):
                    charCounts.pop(s[i])
            
        return len(charCounts) == 0