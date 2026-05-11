# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        
        q = deque()
        temp = root
        q.append(temp)

        while len(q) > 0:
            n = len(q)
            level = []
            for i in range(n):
                frnt = q.popleft()
                level.append(frnt.val)
                
                if frnt.left:
                    q.append(frnt.left)
                
                if frnt.right:
                    q.append(frnt.right)
            
            ans.append(level)
        
        return ans
