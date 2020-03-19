# -*- coding: utf-8 -*-
# @Time : 2020/3/19 16:09
# @Author : leehour
# @File : 39_Recover Rotated Sorted Array.py
# @Software: PyCharm
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i + 1, len(nums) - 1)
                self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1