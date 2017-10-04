#2017/10/3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res, nodes = [], [root] if root else []
        while nodes:
            res.append(list(node.val for node in nodes))
            nodes = [x for node in nodes for x in (node.left, node.right) if x] # This is like two-layers for loop
        res.reverse()
        return res
