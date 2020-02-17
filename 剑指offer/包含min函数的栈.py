# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)
        if not self.stack2 or node < self.stack2[-1]:
            self.stack2.append(node)
        else:
            self.stack2.append(self.stack2[-1])

    def pop(self):
        # write code here
        if self.stack1:
            self.stack1.pop(-1)
            return self.stack2.pop(-1)
        return None

    def top(self):
        # write code here
        if self.stack1:
            return self.stack1[-1]
        return None

    def min(self):
        # write code here
        if self.stack2:
            return self.stack2[-1]
        return None