class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, curr, currSum):
            if i >= len(nums) or currSum > target:
                return

            if currSum == target:
                ans.append(curr)
                return

            dfs(i + 1, curr, currSum)

            acc = curr + [nums[i]]
            accSum = currSum + nums[i]
            dfs(i, acc, accSum)

        
        dfs(0, [], 0)
        return ans

        