'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        left_to_right = True
        res = []
        if root is None:
            return []
        queue.append(root)
        while queue:
            level_size = len(queue)
            result = []
            for i in range (level_size):
                e = queue.popleft()
                if left_to_right:
                    result.append(e.val)
                else:
                    result.insert(0,e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(result)
            left_to_right = not left_to_right
        return res
