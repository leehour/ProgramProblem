# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        first, second, third = 1, 2, 0
        for i in range(3, number + 1):
            third = first + second
            first, second = second, third
        return third

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(4))