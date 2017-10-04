#2017/10/3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            return not q
        if not q:
            return not p
        if p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False