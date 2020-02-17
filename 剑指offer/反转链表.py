# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        pre_node, next_node = None, None
        while pHead:
            next_node = pHead.next
            pHead.next = pre_node

            pre_node = pHead
            pHead = next_node
        return pre_node