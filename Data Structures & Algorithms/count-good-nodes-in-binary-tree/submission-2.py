# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## USE DEQUE CHECK HOW TO
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0
        def dfs(node, currMax):
            nonlocal ans
            if node is None:
                return

            if node.val >= currMax:
                ans += 1
                currMax = node.val

            dfs(node.left, currMax)
            dfs(node.right, currMax)




        dfs(root, -1001)
        return ans
        




