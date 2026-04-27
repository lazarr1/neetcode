class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        count = {}

        l = 0
        for r in range(len(s2)):
            count[s2[r]] = count.get(s2[r], 0) + 1

            
            while r - l + 1 > len(s1):
                count[s2[l]] -= 1
                if (count[s2[l]] == 0):
                    count.pop(s2[l])
                l += 1

            print(count)
            if target == count:
                return True


        return False
        