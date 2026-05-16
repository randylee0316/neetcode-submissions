# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, 100000, -100000)]

        while stack:
            node, M, m = stack.pop()
            if node.left:
                if node.left.val >= node.val or node.left.val <= m:
                    return False
                stack.append((node.left, min(M, node.val), m))
            if node.right:
                if node.right.val <= node.val or node.right.val >= M:
                    return False
                stack.append((node.right, M, max(m, node.val)))

        return True