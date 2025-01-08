'''
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
class Solution:
    def maxDepth(self,root):
        if root is None:
            return True
        leftheight = self.maxDepth(root.left)
        if leftheight == -1:
            return -1
        rightheight = self.maxDepth(root.right)
        if rightheight == -1:
            return -1
        if abs(leftheight - rightheight) > 1:
            return -1
        return 1 + max(leftheight,rightheight)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        ans = self.maxDepth(root)
        if ans >= 0:
            return True
        return False
