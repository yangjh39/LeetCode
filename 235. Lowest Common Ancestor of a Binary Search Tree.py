# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 13:48
# @Author  : Jiahao Yang
# @Email   : yangjh39@uw.edu

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return []

        ma = max(p.val, q.val)
        mi = min(p.val, q.val)

        if root.val > ma:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < mi:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

