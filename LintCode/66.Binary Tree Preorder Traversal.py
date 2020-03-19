# -*- coding: utf-8 -*-
# @Time : 2020/3/19 16:24
# @Author : leehour
# @File : 66.Binary Tree Preorder Traversal.py
# @Software: PyCharm
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
    @return: Preorder in ArrayList which contains node values.
    """

    # def preorderTraversal(self, root):
    #     # write your code here

    #     results = []
    #     self.preorder(results, root)
    #     return results

    # def preorder(self, results, root):
    #     if not root:
    #         return

    #     results.append(root.val)
    #     self.preorder(results, root.left)
    #     self.preorder(results, root.right)

    def preorderTraversal(self, root):
        if not root:
            return []
        stack = []
        results = []
        stack.append(root)
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return results