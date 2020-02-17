class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack1 = []
        while pushV:
            stack1.append(pushV.pop(0))
            while stack1 and popV[0] == stack1[-1]:
                    stack1.pop(-1)
                    popV.pop(0)
        if not stack1:
            return True
        return False


if __name__ == '__main__':
   s = Solution()
   push_v = [1,2,3,4,5]
   pop_v = [4,5,3,2,1]
   pop_v_2 = [4,3,5,1,2]
   print(s.IsPopOrder(push_v, pop_v))