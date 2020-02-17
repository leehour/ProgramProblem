class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        temp = []
        temp.append(root)
        while temp:
            result.append(temp[0].val)
            if temp[0].left:
                temp.append(temp[0].left)
            if temp[0].right:
                temp.append(temp[0].right)
            temp.pop(0)
        return result