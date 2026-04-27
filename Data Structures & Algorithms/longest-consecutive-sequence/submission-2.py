class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        ans = 0 
        for num in nums:
            if num - 1 not in num_set:
                curr = 1
                temp = num

                while num + 1 in num_set:
                    curr += 1
                    num += 1

                ans = max(ans, curr)

        return ans