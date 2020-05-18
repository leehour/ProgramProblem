#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 21:45
# @Author  : leehour
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        temp = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in temp:
                i = max(temp[s[j]], i)
            ans = max(ans, j - i + 1)
            temp[s[j]] = j + 1
        return ans