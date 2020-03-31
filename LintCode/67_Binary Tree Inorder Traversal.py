#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 8:01
# @Author  : leehour
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
    @return: Inorder in ArrayList which contains node values.
    """

    # def inorderTraversal(self, root):
    #     # write your code here

    #     results = []
    #     self.inorder(results, root)
    #     return results

    # def inorder(self, results, root):
    #     if not root:
    #         return

    #     self.inorder(results, root.left)
    #     results.append(root.val)
    #     self.inorder(results, root.right)

    def inorderTraversal(self, root):
        stack = []
        results = []
        curt = root
        while curt or stack:
            while curt:
                stack.append(curt)
                curt = curt.left
            curt = stack.pop()
            results.append(curt.val)
            curt = curt.right
        return results
