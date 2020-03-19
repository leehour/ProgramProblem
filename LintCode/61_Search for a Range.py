# -*- coding: utf-8 -*-
# @Time : 2020/3/19 15:37
# @Author : leehour
# @File : 61_Search for a Range.py
# @Software: PyCharm

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]

        leftBound, rightBound = 0, 0
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            leftBound, rightBound = -1, -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            rightBound = end
        elif A[start] == target:
            rightBound = start
        return [leftBound, rightBound]