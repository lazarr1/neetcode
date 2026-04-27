class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lut = {}
        for i in range(len(nums)):
            lut[nums[i]] = i

        for i in range(len(nums)):
            if ((target - nums[i]) in lut) and (i != lut[target - nums[i]]):
                return [i, lut[target - nums[i]]]
        