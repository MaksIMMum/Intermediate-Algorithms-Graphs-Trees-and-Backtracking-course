
class Solution:
    def isValidBST(self, root):

        io_list_val = []

        self.helper(root, io_list_val)

        is_bst = True

        prev = io_list_val[0]

        for i in range(1, len(io_list_val)):

            if io_list_val[i] <= prev:
                is_bst = False
            prev = io_list_val[i]

        return is_bst

    def helper(self, TreeNode, io_list_val):

        if TreeNode is None:
            return

        self.helper(TreeNode.left, io_list_val)

        io_list_val.append(TreeNode.val)

        self.helper(TreeNode.right, io_list_val)
