# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or len(array) == 0:
            return False
        row = 0
        column = len(array[0]) - 1
        while row < len(array) and column >= 0:
            number = array[row][column]
            if number == target:
                return True
            elif number < target:
                row += 1
            else:
                column -= 1
        return False
