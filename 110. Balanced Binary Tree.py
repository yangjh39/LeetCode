#2017/10/6

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def treedeep(self, node):
        if not node:
            return 0

        deep = 1

        if node.left or node.right:
            deep = 1 + max(self.treedeep(node.left), self.treedeep(node.right))

        return deep

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        print()

        return abs(self.treedeep(root.left) - self.treedeep(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

temp = Solution()
temp.isBalanced(root)