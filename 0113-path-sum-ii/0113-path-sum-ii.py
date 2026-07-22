from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node: Optional[TreeNode], path: List[int], remaining: int):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])
            else:
                dfs(node.left, path, remaining)
                dfs(node.right, path, remaining)
            path.pop()
        
        dfs(root, [], targetSum)
        return res
