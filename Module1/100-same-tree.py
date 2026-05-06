
class Solution:
    def isSameTree(self, p, q):

        if p == None and q == None:
            return True

        if p == None or q == None or p.val != q.val:
            return False

        left_compare_val = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare_val and right_compare
