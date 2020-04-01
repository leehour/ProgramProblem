#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 7:53
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
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1