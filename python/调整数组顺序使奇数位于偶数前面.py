# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd, even = [], []
        for i in range(len(array)):
            odd.append(array[i]) if array[i] % 2 == 1 else even.append(array[i])
        return odd + even