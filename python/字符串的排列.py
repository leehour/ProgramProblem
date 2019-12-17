class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        result = []
        visited = [0] * len(ss)
        self.helper(result, '', visited, ss)
        return sorted(list(set(result)))

    def helper(self, result, path, visited, ss):
        if len(path) == len(ss):
            result.append(path)
            return
        for i in range(len(ss)):
            if not visited[i]:
                visited[i] = 1
                self.helper(result, path + ss[i], visited, ss)
                visited[i] = 0


# -*- coding:utf-8 -*-
# 参考：https://blog.csdn.net/fuxuemingzhu/article/details/79513101
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if not ss:
#             return []
#         result = []
#         self.helper(result, '', ss)
#         return sorted(list(set(result)))
#
#     def helper(self, result, path, ss):
#         if not ss:
#             result.append(path)
#             return
#         for i in range(len(ss)):
#             self.helper(result, path + ss[i], ss[:i] + ss[i + 1:])