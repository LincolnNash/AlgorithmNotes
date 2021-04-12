"""
# 判断平衡二叉树 https://leetcode-cn.com/problems/balanced-binary-tree/
    给定一个二叉树，判断它是否是高度平衡的二叉树。
    平衡二叉树定义：给定二叉树的每个节点的左右子树高度差小于或等于1
"""
class Solution1(object):
    """
    自上而下的遍历,时间复杂度O(n2)
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1

    def height(self, root):
        """
        :param root:
        :return: height
        """
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


class Solution2():
    """
    自底向上法：在求子树的高度过程如果出现了，不满足平衡二叉树则该树不是平衡二叉树。
    """
    def isBalance(self, root):
        def height(root):
            if root == None:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)
            if leftheight == -1 or rightheight == -1 or abs(leftheight-rightheight) > 1:
                return -1
            else:
                return max(leftheight, rightheight) + 1
        return height(root) >= 0