import unittest
from binary_tree_lab import TreeNode, max_depth, lowest_common_ancestor

class TestBinaryTreeFunctions(unittest.TestCase):
    def test_max_depth(self):
        # Construct the binary tree
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(max_depth(root), 3)

    def test_lowest_common_ancestor(self):
        # Construct the BST
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        p = root.left  # Node with value 2
        q = root.right  # Node with value 8

        lca = lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val, 6)

if __name__ == '__main__':
    unittest.main()
