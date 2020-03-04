#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 7:45
# @Author  : leehour

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        result = []
        temp = []
        self.subsetHelper(result, temp, nums, 0)
        return result

    def subsetHelper(self, result, temp, nums, pos):
        result.append(temp[:])
        for i in range(pos, len(nums)):
            temp.append(nums[i])
            self.subsetHelper(result, temp, nums, i + 1)
            temp.pop(-1)

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))