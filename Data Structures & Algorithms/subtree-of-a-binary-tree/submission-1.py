# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            stack = [(a, b)]
            while stack:
                a, b = stack.pop()
                if not a and not b:
                    continue
                if not a or not b or a.val != b.val:
                    return False
                stack.append((a.right, b.right))
                stack.append((a.left, b.left))
            return True

        if not subRoot:
            return True
        if not root:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node == None:
                continue
            if isSame(node, subRoot):
                return True
            stack.append(node.right)
            stack.append(node.left)
        return False