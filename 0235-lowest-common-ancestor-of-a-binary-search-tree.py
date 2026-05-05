
class Solution:
    def lowestCommonAncestor(self, root, p_val, q_val):
        while root:

            if p_val.val > root.val and q_val.val > root.val:
                root = root.right

            elif p_val.val < root.val and q_val.val < root.val:
                root = root.left

            else:

                return root
