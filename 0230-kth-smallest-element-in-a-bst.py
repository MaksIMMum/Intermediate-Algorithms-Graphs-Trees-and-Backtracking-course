
class Solution:
    def kthSmallest(self, root, k_idx):

        io_list = []

        self.helper(root, io_list)

        return io_list[k_idx-1]

    def helper(self, TreeNode, io_list):

        if TreeNode is None:
            return

        self.helper(TreeNode.left, io_list)
        io_list.append(TreeNode.val)
        self.helper(TreeNode.right, io_list)
