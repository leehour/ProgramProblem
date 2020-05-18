#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 21:16
# @Author  : leehour
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        leftNum = (n + m + 1) // 2
        rightNum = (n + m + 2) // 2
        return (self.findSortedArrays(nums1, 0, nums2, 0, leftNum) + self.findSortedArrays(nums1, 0, nums2, 0, rightNum)) / 2.0

    def findSortedArrays(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]

        if k == 1:
            return min(nums1[i], nums2[j])

        midVal1 = float("inf")
        midVal2 = float("inf")
        if i + k // 2 - 1 < len(nums1):
            midVal1 = nums1[i + k // 2 - 1]
        if j + k // 2 - 1 < len(nums2):
            midVal2 = nums2[j + k // 2 - 1]
        if midVal1 < midVal2:
            return self.findSortedArrays(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.findSortedArrays(nums1, i, nums2, j + k // 2, k - k // 2)


if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    s = Solution()
    print(s.findMedianSortedArrays(a, b))
