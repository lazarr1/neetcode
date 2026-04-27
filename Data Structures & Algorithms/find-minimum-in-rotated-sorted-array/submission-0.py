class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        curr = nums[0]
        while l <= r:

            mid = (l + r) // 2
            curr = min(curr, nums[mid])
            if (nums[l] >= nums[r]):
                l = mid + 1
            elif (nums[l] < nums[r]):
                r = l
                l = 0

        return curr