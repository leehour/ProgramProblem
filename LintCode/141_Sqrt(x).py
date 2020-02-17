#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 0:16
# @Author  : leehour
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def sqrt(self, x):
        # write your code here
        if x == 0 or x == 1:
            return x

        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid < x / mid:
                start = mid
            elif mid > x / mid:
                end = mid
            else:
                return mid

        if start * start <= x:
            return start
        else:
            return end
