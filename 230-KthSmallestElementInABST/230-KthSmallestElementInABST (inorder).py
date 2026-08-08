# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        realized inorder for BST is essentially alr sorted

        1 ms runtime beats 40%, but same as optimal 0 ms.

        THis is better because it doesnt rely on O(nlogn) sort function. this is O(n) instead as it traverses all nodes
        """

        arr = []
        
        def bfs(root):
            if not root:
                return
            bfs(root.left)
            arr.append(root.val)
            bfs(root.right)

        bfs(root)

        return arr[k-1]
