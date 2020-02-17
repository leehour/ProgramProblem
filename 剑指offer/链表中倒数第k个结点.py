# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        first = head
        last = head
        for i in range(k - 1):
            if not last.next:
                return None
            last = last.next
        while last.next:
            first = first.next
            last = last.next
        return first