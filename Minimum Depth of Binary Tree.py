#2017/10/6

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        #
        # deep = 1
        #
        # if root.left and root.right:
        #     deep = deep + min(self.minDepth(root.left), self.minDepth(root.right))
        # elif root.left:
        #     deep = deep + self.minDepth(root.left)
        # elif root.right:
        #     deep = deep + self.minDepth(root.right)
        #
        # return deep

        if not root:
            return 0

        d = map(self.minDepth, (root.left, root.right))

        return 1 + (min(d) or max(d))



