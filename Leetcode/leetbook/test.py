# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.left is not None:
                stack.append(curr)
                stack.append(curr.left)
                continue
            result.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
        return result
a = [[3],[9,20],[15,7]]
a[1].reverse()