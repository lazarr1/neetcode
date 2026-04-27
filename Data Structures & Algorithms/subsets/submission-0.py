class Solution:
    def subsets(self, arr):
        ans = [[]]
        
        for i in range(len(arr)):
            for j in range(len(ans)):
                ans.append(ans[j] + [arr[i]])

        return ans


