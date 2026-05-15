# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        add = []

        while q:
            node = q.popleft()
            if node == None:
                continue
            add.append(node.val)

            if node.left != None: 
                q.append(node.left)
            if node.right != None: 
                q.append(node.right)
            if node == root:
                res.append(add)
                add = []
                root = q[-1] if q else None
        
        return res

            

