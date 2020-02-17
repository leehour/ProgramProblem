# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.is_subtree(pRoot1.left, pRoot2) or self.is_subtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, node1, node2):
        # 1. 子树只要包含了一个结点，就得包含这个结点下的所有节点。因此，A树与其子树一定最后同时访问到空指针。
        # 2. 子结构只要包含任意相连的任意数量的结点即可。
        # 因此，对于子结构而言，只要在子结构访问到空指针之前，所有的节点均和A树的某部分相同就可以了。
        # 如果这里是子树，则应该只要包含了一个结点，就得包含这个结点下的所有节点。因此，A树与其子树一定最后同时访问到空指针。
        # 这两行应该改为：
        # if not node1 and not node2:
        #     return true
        if not node2:
            return True
        if not node1:
            return False
        if node1.val == node2.val:
            return self.is_subtree(node1.left, node2.left) and self.is_subtree(node1.right, node2.right)
        return False
