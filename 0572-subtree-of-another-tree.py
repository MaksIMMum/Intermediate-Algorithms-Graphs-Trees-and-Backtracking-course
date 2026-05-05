
class Solution:

    def isSubtree(self, root, sub_root):

        if sub_root is None:
        	return True

        if root == None and sub_root != None:
        	return False

        if self.isSameTree(root, sub_root):
        	return True

        left_check = self.isSubtree(root.left, sub_root)
        right_check = self.isSubtree(root.right, sub_root)

        return left_check or right_check

    def isSameTree(self, p, q):
        if p == None and q == None:
        	return True

        if p == None or q == None or p.val != q.val:
        	return False

        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare and right_compare
