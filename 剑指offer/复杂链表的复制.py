# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# 假设原链表为 1 -> 2 -> 3 -> 4
# 分三步：
# 第一步：把每个链表节点复制一份接到原节点后1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4
# 第二步：设置新加入节点的random节点，关键步骤为：node.next.random = node.random.next
# 第三步：将新加入节点抽离出来变成单独的链表
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        p_temp = pHead
        while p_temp:
            node_temp = RandomListNode(p_temp.label)
            node_temp.next = p_temp.next
            p_temp.next = node_temp
            p_temp = node_temp.next

        p_temp = pHead
        while p_temp and p_temp.next:
            if p_temp.random:
                p_temp.next.random = p_temp.random.next
            p_temp = p_temp.next.next

        p_temp = pHead
        p_now = pHead.next
        while p_temp:
            node = p_temp.next
            p_temp.next = node.next
            if node.next:
                node.next = node.next.next
            p_temp = p_temp.next
        return p_now


if __name__ == '__main__':
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = node3
    node2.random = node2
    node3.random = node4
    node4.random = node1
    s = Solution()
    new_node = s.Clone(node1)
    while new_node:
        print(new_node.label)
        new_node = new_node.next
