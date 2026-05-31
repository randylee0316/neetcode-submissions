"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        counter = 0
        used = {}
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr not in used:
                node = Node(curr.val)
                used[curr] = node
            else:
                node = used[curr]

            if counter == 0:
                res = node
            counter += 1
            for i in curr.neighbors:
                if i != None:
                    if i not in used:
                        neighbor = Node(i.val)
                        node.neighbors.append(neighbor)
                        used[i] = neighbor
                        q.append(i)
                    else:
                        node.neighbors.append(used[i])


        
        return res

