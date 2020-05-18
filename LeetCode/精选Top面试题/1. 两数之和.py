#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 21:32
# @Author  : leehour
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i
