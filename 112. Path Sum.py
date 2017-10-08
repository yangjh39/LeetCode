#2017/10/7

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def cal(self, root):
    #     if not root:
    #         return 0
    #
    #     num = root.val
    #
    #     if root.left and root.right:
    #         a = self.cal(root.left);b = self.cal(root.right)
    #         num = [x + root.val for x in [a if type(a) == list else [a] + b if type(b) == list else [b]]]
    #     elif root.left:
    #         num = [x + root.val for x in [self.cal(root.left)]]
    #     elif root.right:
    #         num = [x + root.val for x in [self.cal(root.right)]]
    #
    #     return num

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

a = TreeNode(1)
temp = Solution()
temp.hasPathSum(a, 1)