
class Solution:
    def maxDepth(self, root_val):
        if not root_val:
            return 0

        max_depth = 0

        stack = [(root_val, 1)]

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return max_depth
