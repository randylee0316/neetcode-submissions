# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root
        stack = []
        depths = {}
        last = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    lheight = depths.get(node.left, 0)
                    rheight = depths.get(node.right, 0)
                    if abs(lheight - rheight) > 1:
                        return False
                    depths[node] = max(lheight, rheight) + 1
                    last = node
                    node = None

                else:
                    node = node.right
        return True


        



        