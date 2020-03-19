# -*- coding: utf-8 -*-
# @Time : 2020/3/19 16:05
# @Author : leehour
# @File : 75_Find Peak Element.py
# @Software: PyCharm
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return end
        else:
            return start