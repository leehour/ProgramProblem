# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        head = None
        current = None
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                if not head:
                    head = current = pHead2
                else:
                    current.next = pHead2
                    current = current.next
                pHead2 = pHead2.next
            else:
                if not head:
                    head = current = pHead1
                else:
                    current.next = pHead1
                    current = current.next
                pHead1 = pHead1.next
        if pHead1:
            current.next = pHead1
        else:
            current.next = pHead2
        return head
