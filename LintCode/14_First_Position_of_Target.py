#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 21:04
# @Author  : leehour
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here

        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] >= target:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
