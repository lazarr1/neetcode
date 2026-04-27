class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lut = {}

        for num in nums:
            if num in lut:
                return True

            lut[num] = True

        return False        