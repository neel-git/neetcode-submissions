# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, ans: List[int], root: Optional[TreeNode]) -> None:
        if root == None:
            return ans
        
        self.helper(ans, root.left)
        self.helper(ans, root.right)
        ans.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(ans, root)

        return ans