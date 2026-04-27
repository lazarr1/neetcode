# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        test = {}

        p = p.val
        q = q.val

        head = root
        while head.val != p:
            test[head.val] = True

            if p > head.val:
                head = head.right
            else:
                head = head.left

        test[head.val] = True
        print(test)

        head = root
        currAncestor = head
        while head.val != q:
            if head.val in test:
                currAncestor = head
            
            if q > head.val:
                head = head.right
            else:
                head = head.left
                
        if head.val in test:
            currAncestor = head
        return currAncestor












