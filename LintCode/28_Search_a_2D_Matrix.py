class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        """
        二分法
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False

        row, column = len(matrix), len(matrix[0])
        start, end = 0, row * column - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            num = matrix[mid // column][mid % column]
            if num < target:
                start = mid
            elif num > target:
                end = mid
            else:
                return True
        return matrix[start // column][start % column] == target or matrix[end // column][end % column] == target

    def searchMatrix2(self, matrix, target):
        """
        直接查找
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False

        row, column = 0, len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1

        return False