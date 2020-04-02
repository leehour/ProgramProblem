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

# // Version 2: without ResultType
# public class Solution {
#     public boolean isBalanced(TreeNode root) {
#         return maxDepth(root) != -1;
#     }
#
#     private int maxDepth(TreeNode root) {
#         if (root == null) {
#             return 0;
#         }
#
#         int left = maxDepth(root.left);
#         int right = maxDepth(root.right);
#         if (left == -1 || right == -1 || Math.abs(left-right) > 1) {
#             return -1;
#         }
#         return Math.max(left, right) + 1;
#     }
# }