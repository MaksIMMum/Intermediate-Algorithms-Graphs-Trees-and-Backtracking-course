
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result_val, queue = [], [root]

        while queue:

            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result_val.append(level)

        return result_val
