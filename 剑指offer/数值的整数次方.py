# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 1:
            return 1
        if exponent == 0:
            return 1
        result = 1
        expo = abs(exponent)
        temp = base
        while expo != 0:
            if expo & 1 == 1:
                result *= temp
            expo = expo >> 1
            temp *= temp
        if exponent > 0:
            return result
        return 1 / result