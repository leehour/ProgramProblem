#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 21:33
# @Author  : leehour

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        head = result
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sumNum = num1 + num2 + carry
            carry = sumNum // 10
            result.next = ListNode(sumNum % 10)
            result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            result.next = ListNode(carry)
        return head.next
