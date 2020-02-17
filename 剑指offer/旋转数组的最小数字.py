# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        target = rotateArray[-1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if rotateArray[mid] <= target:
                right = mid
            else:
                left = mid
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[left]
        return rotateArray[right]


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([ 3, 1, 2]))
