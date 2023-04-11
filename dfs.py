# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def depthFirstSearch(root, targetSum, runningSum) -> bool:
            if root:
                runningSum += root.val
                if runningSum == targetSum and root.left == None and root.right == None:
                    return True
                left = depthFirstSearch(root.left, targetSum, runningSum)
                right = depthFirstSearch(root.right, targetSum, runningSum)

                return left or right
            return False

        return depthFirstSearch(root, targetSum, 0)