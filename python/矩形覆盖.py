# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        # 类似于裴波那契数列
        if number <= 2:
            return number
        res = [0, 1, 2]
        for i in range(3, number + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[-1]