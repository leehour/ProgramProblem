"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here

        if not root:
            return []

        nodes = [root]
        results = []
        while nodes:
            tempList = []
            for i in range(len(nodes)):
                node = nodes.pop(0)
                tempList.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            results.append(tempList)

        return results