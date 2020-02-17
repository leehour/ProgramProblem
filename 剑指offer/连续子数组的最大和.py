# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        max_sum = array[0]
        sum_array = 0
        for i in array:
            sum_array += i
            if max_sum < sum_array:
                max_sum = sum_array
            if sum_array < 0:
                sum_array = 0
        return max_sum