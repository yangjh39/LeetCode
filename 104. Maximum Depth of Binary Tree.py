#2017/10/3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

root = TreeNode(1)
root.left = TreeNode(2)


temp = Solution()
temp.maxDepth(root)