#使用快排中的partition思想。
# 选取一个key = tinput[0], 先进行一轮排序，比key大的在左边，小的在右边,返回此时的left值。
# 如果left比key大，则把缩小查找范围在key左半边查找
# 如果left比key小，则把缩小查找范围在key右半边查找
# 注意边界条件：数组为空或者k比数组长度大时，返回[]

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or not tinput:
            return []
        length = len(tinput)
        left = 0
        right = length - 1
        index = self.getPartition(tinput, left, right)
        while k != index:
            if index > k - 1:
                right = index - 1
            else:
                left = index + 1
            if left < len(tinput):
                index = self.getPartition(tinput, left, right)
            else:
                break
        result = tinput[0:k]
        result.sort()
        return result

    def getPartition(self, lists, left, right):
        # 划分函数处理部分
        key = lists[left]
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
        lists[left] = key
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.GetLeastNumbers_Solution([],0))
