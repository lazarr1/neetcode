class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        zero_count = 0
        for num in nums:
            if (num != 0):
                res *= num
            else:
                zero_count += 1

        ans = []
        for num in nums:
            if zero_count == 0:
                if num != 0:
                    ans.append(int(res/num))
            elif zero_count >= 2:
                ans.append(0)
            else :
                if num == 0:
                    ans.append(res)
                else:
                    ans.append(0)
        return ans