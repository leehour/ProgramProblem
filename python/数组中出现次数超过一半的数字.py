# -*- coding:utf-8 -*-
class Solution:
    '''
    链接：https://www.nowcoder.com/questionTerminal/e8a1b01a2df14cb2b228b30ee6a92163?f=discussion
    来源：牛客网
    如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多。
    在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；
    若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。
    然后再判断它是否符合大于一半数字的条件即可(否则如12345666也不满足条件)。
    时间复杂度为O(n)
    '''
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        count = 1
        temp = numbers[0]
        for i in range(1, len(numbers) - 1):
            if temp != numbers[i]:
                if count == 0:
                    temp = numbers[i]
                    count = 1
                else:
                    count -= 1
            else:
                count += 1
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == temp:
                count += 1
        if count > len(numbers) // 2:
            return temp
        return 0
