#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 8:07
# @Author  : leehour
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        result = []
        temp = []
        self.subsetsHelper(nums, result, temp, 0)
        return result

    def subsetsHelper(self, nums, result, temp, pos):
        result.append(temp[:])
        for i in range(pos, len(nums)):
            if i != pos and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.subsetsHelper(nums, result, temp, i + 1)
            temp.pop(-1)

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2, 3]))