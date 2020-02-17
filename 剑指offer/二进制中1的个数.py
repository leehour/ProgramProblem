# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 剑指offer 中的负数取补码时需要 & 0xffffffff,java不用
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-1))