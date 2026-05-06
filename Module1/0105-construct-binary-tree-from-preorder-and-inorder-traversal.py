
class Solution:
    def buildTree(self, preorder, inorder):

        io_map = {}
        for i in range(len(inorder)):
            io_map[inorder[i]] = i

        return self.splitTree(preorder, io_map, 0, 0, len(inorder) - 1)

    def splitTree(self, preorder, io_map, root_index, left, right):

        if left > right:
            return None

        root = TreeNode(preorder[root_index])

        mid = io_map[preorder[root_index]]

        if mid > left:
            root.left = self.splitTree(preorder, io_map, root_index + 1, left, mid - 1)

        if mid < right:
            root.right = self.splitTree(preorder, io_map, root_index + mid - left + 1, mid + 1, right)

        return root
