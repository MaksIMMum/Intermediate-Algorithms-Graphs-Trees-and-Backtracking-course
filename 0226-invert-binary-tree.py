
class Solution:
    def invertTree(self, root_val):

        if root_val is None:
            return None

        root_val.left, root_val.right = root_val.right, root_val.left

        self.invertTree(root_val.left)
        self.invertTree(root_val.right)

        return root_val
