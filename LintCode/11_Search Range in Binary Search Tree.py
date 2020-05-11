#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 8:05
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        arr = []
        self.helper(root, k1, k2, arr)
        return arr

    def helper(self, root, k1, k2, arr):
        if not root:
            return
        if root.val > k1:
            self.helper(root.right, k1, k2, arr)
        if root.val < k2:
            self.helper(root.left, k1, k2, arr)
        if root.val >= k1 and root.val <= k2:
            arr.append(root.val)