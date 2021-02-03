#二叉树的遍历
from collections import deque
class Solution(object):
    def __init__(self):
        self.ans = []

    def preorderTraversal_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.ans.append(root.val)
        self.inorderTraversal(root.left)
        self.inorderTraversal(root.right)
        return self.ans


    def inorderTraversal_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return self.ans

    def postorderTravelsal_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.postorderTravelsal_recur(root.left)
        self.postorderTravelsal_recur(root.right)
        self.ans.append(root.val)
        return self.ans

    def preorderTravelsal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if root is not None:
            stack.append(root)
        while len(stack)>0:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

    def inorderTraversal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        while curr and len(stack)>0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    def postorderTravelsal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        prev = None
        while len(stack)>0 or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            #如果右节点不存在或者右节点已经被访问
            if curr.right and prev == curr.right:
                result.append(curr.val)
                prev = curr
                curr = None
            else:
                stack.append(curr)
                curr = curr.right
        return result

    #锯齿形层序遍历二叉树
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        dq = deque()
        count = 0
        if root is not None:
            dq.append(root)
            count = 1
        while len(dq)>0:
            temp = 0
            container = []
            for _ in range(count):
                curr = dq.popleft()
                container.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                    temp+=1
                if curr.right:
                    dq.append(curr.right)
                    temp+=1
            result.append(container)
            count = temp
        for i in range(len(result)):
            if (i % 2) == 1:
                result[i].reverse()
        return result

    #从中序与后序遍历序列构造二叉树
    

