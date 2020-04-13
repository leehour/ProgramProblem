#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 7:46
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []

        result = []
        nodes = []
        nodes.append(root)
        while nodes:
            tempList = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                tempList.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.insert(0, tempList)
        return result

