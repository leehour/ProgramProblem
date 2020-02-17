# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or not matrix[0]:
            return []
        row = len(matrix)
        col = len(matrix[0])
        result = []
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result


if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11,12],[13, 14, 15, 16]]
    s = Solution()
    print(s.printMatrix(mat))