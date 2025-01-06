from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # Ліве піддерево повне
            return (2 ** left_height) + self.countNodes(root.right)
        else:
            # Праве піддерево повне
            return (2 ** right_height) + self.countNodes(root.left)
