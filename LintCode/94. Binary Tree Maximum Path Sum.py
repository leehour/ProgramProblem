#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 7:52
# @Author  : leehour
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here

        self.maxSum = -sys.maxsize

        self.helper(root)

        return self.maxSum

    def helper(self, root):

        if root:
            left = max(self.helper(root.left), 0)
            right = max(self.helper(root.right), 0)
            self.maxSum = max(self.maxSum, left + root.val + right)
            return max(root.val + left, root.val + right)
        else:
            return -1
