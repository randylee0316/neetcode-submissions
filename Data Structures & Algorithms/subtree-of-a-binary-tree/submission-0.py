class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            stack = [(a, b)]

            while stack:
                x, y = stack.pop()

                # both empty
                if not x and not y:
                    continue

                # one empty or values differ
                if not x or not y or x.val != y.val:
                    return False

                stack.append((x.left, y.left))
                stack.append((x.right, y.right))

            return True

        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                continue

            if sameTree(node, subRoot):
                return True

            stack.append(node.left)
            stack.append(node.right)

        return False