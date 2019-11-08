# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # f(n) = f(n - 1) + f(n - 2) + ... + f(1) + 1
        # f(n - 1) = f(n - 2) + f(n - 3) + ... + f(1) + 1
        # f(n) - f(n - 1) = f(n - 1) => f(n) = 2 * f(n - 1)等比数列
        # f(n) = 2^(n - 1)
        # return 2 ** (number - 1)
        return 1 << (number - 1)