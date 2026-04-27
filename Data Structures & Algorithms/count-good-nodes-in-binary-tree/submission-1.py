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
        def dfs(node, maxStack):
            nonlocal ans
            clear = False
            if node is None:
                return

            if not maxStack or node.val >= maxStack[-1]:
                ans += 1
                maxStack.append(node.val)
                clear = True

            dfs(node.left, maxStack)
            dfs(node.right, maxStack)

            if clear:
                maxStack.pop()



        dfs(root, [])
        return ans
        




