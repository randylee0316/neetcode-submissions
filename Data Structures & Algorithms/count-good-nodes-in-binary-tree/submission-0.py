# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        c = 1
        while stack:
            node, m = stack.pop()
            if node:
                if node.right:
                    if node.right.val >= m:
                        c += 1
                    stack.append((node.right, max(m, node.right.val)))
                if node.left:
                    if node.left.val >= m:
                        c += 1
                    stack.append((node.left, max(m, node.left.val)))

        return c