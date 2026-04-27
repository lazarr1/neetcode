class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ans = 0
        lut = {}
        for num in nums:
            lut[num] = 1
        
        for (key, value) in lut.items():
            curr = 0
            temp = key
            while temp in lut:
                curr += lut[temp]

                if (lut[temp] != 1):
                    break
                temp+=1 

            lut[key] = curr

            ans = max(ans, curr)


        return ans