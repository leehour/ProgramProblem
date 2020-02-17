# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return ""
        str_space = []
        for i in s:
            if i == ' ':
                str_space.append('%')
                str_space.append('2')
                str_space.append('0')
            else:
                str_space.append(i)
        return ''.join(str_space)