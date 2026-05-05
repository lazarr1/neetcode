class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # CASE 1: exclude last → [0 ... n-2]
        currentLoot = nums.copy()
        currentLoot[-1] = 0

        for i in range(len(nums) - 3, -1, -1):
            currentLoot[i] = max(currentLoot[i + 1], nums[i] + currentLoot[i + 2])

        cost1 = currentLoot[0]


        # CASE 2: exclude first → [1 ... n-1]
        currentLoot = nums.copy()
        currentLoot[0] = 0
        currentLoot[-2] = max(currentLoot[-2], currentLoot[-1])

        for i in range(len(nums) - 3, -1, -1):
            currentLoot[i] = max(currentLoot[i + 1], nums[i] + currentLoot[i + 2])

        cost2 = currentLoot[1]


        return max(cost1, cost2)