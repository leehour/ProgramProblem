# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        root = sequence[-1]
        length = len(sequence)
        for i in range(0, length):
            if sequence[i] > root:
                break

        for j in range(i, length):
            if sequence[j] < root:
                return False

        left = right = True
        if i > 0:
            self.VerifySquenceOfBST(sequence[0: i])

        if i < length - 1 and left:
            self.VerifySquenceOfBST(sequence[i: -1])
        return left and right


if __name__ == '__main__':
    seq = [4, 5, 2, 6, 7, 3, 1]
    s = Solution()
    print(s.VerifySquenceOfBST(seq))
