# 作者：shine_chan
# 链接：https://www.nowcoder.com/questionTerminal/b736e784e3e34731af99065031301bca?f=discussion
# 来源：牛客网

# public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
#         ArrayList<ArrayList<Integer>> res = new ArrayList<>();
#         if(root == null) return res;
#         backstrack(res, new ArrayList<>(), root, target);
#         return res;
#     }
#
#     public void backstrack(ArrayList<ArrayList<Integer>> res, ArrayList<Integer> list, TreeNode root, int target) {
#         if (target >= root.val) {
#             target = target - root.val;
#             list.add(root.val);
#
#             if (root.left == null && root.right == null && target == 0) {
#                 res.add(new ArrayList<>(list));
#             }
#             if (root.left != null) {
#                 backstrack(res, list, root.left, target);
#             }
#             if (root.right != null) {
#                 backstrack(res, list, root.right, target);
#             }
#             list.remove(list.size() - 1);
#         }
#
#
#     }

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        line = []
        self.dfs(result, line, root, expectNumber)
        return result

    def dfs(self, result, line, root, expectNumber):
        if expectNumber >= root.val:
            expectNumber -= root.val
            line.append(root.val)

            if not root.left and not root.right and expectNumber == 0:
                result.append(line[:])

            if root.left:
                self.dfs(result, line, root.left, expectNumber)
            if root.right:
                self.dfs(result, line, root.right, expectNumber)

            line.pop(-1)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    s = Solution()
    print(s.FindPath(node1, 3))
