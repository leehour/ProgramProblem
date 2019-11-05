# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return ""
        list_value = []
        head = listNode
        while head:
            list_value.append(head.val)
            head = head.next
        list_value.reverse()
        return list_value


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    s = Solution()
    print(s.printListFromTailToHead(a))
