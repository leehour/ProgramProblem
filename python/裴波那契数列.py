# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        first = 1
        second = 1
        for i in range(3, n + 1):
            third = first + second
            first, second = second, third
        return third


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(5))