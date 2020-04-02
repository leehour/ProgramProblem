#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 8:10
# @Author  : leehour
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class ReturnType:
    def __init__(self, isBalanced, maxDepth):
        self.isBalanced = isBalanced
        self.maxDepth = maxDepth

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.helper(root).isBalanced

    def helper(self, root):
        if not root:
            return ReturnType(True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        if not left.isBalanced or not right.isBalanced:
            return ReturnType(False, -1)

        if abs(left.maxDepth - right.maxDepth) > 1:
            return ReturnType(False, -1)

        return ReturnType(True, max(left.maxDepth, right.maxDepth) + 1)
