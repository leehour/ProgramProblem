#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 8:14
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
    @return: Postorder in ArrayList which contains node values.
    """

    # def postorderTraversal(self, root):
    #     # write your code here

    #     results = []
    #     self.postorder(root, results)
    #     return results

    # def postorder(self, root, results):
    #     if not root:
    #         return

    #     self.postorder(root.left, results)
    #     self.postorder(root.right, results)
    #     results.append(root.val)

    def postorderTraversal(self, root):
        """
        后序遍历的非递归版本是从右到左的前序遍历的逆序
        :param root:
        :return:
        """
        stack = []
        results = []
        stack_out = []
        stack.append(root)
        while stack:
            curt = stack.pop()
            stack_out.append(curt.val)
            if curt.left:
                stack.append(curt.left)
            if curt.right:
                stack.append(curt.right)
        while stack_out:
            results.append(stack_out.pop())
        return results