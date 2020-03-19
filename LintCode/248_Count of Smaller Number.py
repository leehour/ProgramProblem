# -*- coding: utf-8 -*-
# @Time : 2020/3/19 15:14
# @Author : leehour
# @File : 248_Count of Smaller Number.py
# @Software: PyCharm
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """

    def countOfSmallerNumber(self, A, queries):
        # write your code here

        A = sorted(A)
        results = []
        for i in queries:
            results.append(self.countNumber(A, i))
        return results

    def countNumber(self, A, number):
        if len(A) == 0 or A[-1] < number:
            return len(A)

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < number:
                start = mid
            else:
                end = mid
        if A[start] >= number:
            return start
        if A[end] >= number:
            return end
        return end + 1