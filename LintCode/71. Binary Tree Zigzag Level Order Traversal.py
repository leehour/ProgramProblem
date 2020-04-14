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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []

        results = []
        nodes = [root]
        level = 0
        while nodes:
            tempList = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                tempList.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if level % 2 == 1:
                tempList = list(reversed(tempList))
            level += 1
            results.append(tempList)
        return results
