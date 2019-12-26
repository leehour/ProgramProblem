# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0
        i = 1
        count = 0
        while i <= n:
            a = n // i
            b = n % i
            h = a % 10
            if h == 0:
                count += a // 10 * i
            elif h == 1:
                count += a // 10 * i + b + 1
            else:
                count += (a // 10 + 1) * i
            i *= 10
        return count
