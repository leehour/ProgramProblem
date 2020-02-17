# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin or len(pre) != len(tin):
            return None
        left_index = 0
        root = TreeNode(pre[0])
        for i in range(len(tin)):
            if tin[i] == pre[0]:
                left_index = i
                break
        right_index = len(pre) - left_index - 1
        if left_index > 0:
            root.left = self.reConstructBinaryTree(pre[1: left_index + 1], tin[: left_index])
        if right_index > 0:
            root.right = self.reConstructBinaryTree(pre[left_index + 1:], tin[left_index + 1:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    print(s.reConstructBinaryTree(pre, tin))

# A better solution
# class Solution:
#     def reConstructBinaryTree(self, pre, tin):
#         if not pre or not tin:
#             return None
#         root = TreeNode(pre.pop(0))
#         index = tin.index(root.val)
#         root.left = self.reConstructBinaryTree(pre, tin[:index])
#         root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
#         return root
