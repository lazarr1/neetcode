# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        h = 0


        if not root:
            return []


        ret = [[root.val]]

        currStack = [root]
        nextStack = []
        curr = []

        while currStack:

            head = currStack[0]

            if head.left:
                nextStack.append(head.left)
                curr.append(head.left.val)
            if head.right:
                nextStack.append(head.right)
                curr.append(head.right.val)

            # print(currStack)
            currStack.pop(0)
            # print(currStack)

            if not currStack and nextStack:
                ret.append(curr)
                curr = []
                currStack = nextStack
                nextStack = []

        return ret
            


        