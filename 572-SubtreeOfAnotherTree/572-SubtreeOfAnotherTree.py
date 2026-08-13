# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    boy am i a dumbass

    will be back.

    39 ms runtiem beats 71%
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root: return False
        if self.is_same(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, r, sr):
        if not r and not sr: return True
        if not r or not sr: return False
        if r.val != sr.val: return False

        return self.is_same(r.left, sr.left) and self.is_same(r.right, sr.right)


        
        
