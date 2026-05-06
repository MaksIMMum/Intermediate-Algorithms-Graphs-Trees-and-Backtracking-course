
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        queue = [root]
        result_val = []
        while queue:
            node = queue.pop(0)
            if node:
                result_val.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result_val.append("N")
        return ",".join(result_val)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
