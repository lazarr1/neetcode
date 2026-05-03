class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] if len(nums) == 1 else 0

        currentLoot = [0] * len(nums)
        currentLoot[-1] = nums[-1]
        currentLoot[-2] = nums[-2]
        # [1, 2, 3, 4]
        # [4]
        # [2]


        for i in range(len(nums) - 3, -1, -1):
            currentLoot[i] = max(currentLoot[i + 1], nums[i] + currentLoot[i + 2])

        return max(currentLoot[0], currentLoot[1])