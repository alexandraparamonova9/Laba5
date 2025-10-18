from main import iterative_binary_tree
import unittest
class TestIterativeBinaryTree(unittest.TestCase):
    def test_height_zero(self):
        self.assertEqual(iterative_binary_tree(height=0, root=10), {"10": []})

    def test_negative_height(self):
        self.assertEqual(iterative_binary_tree(height=-1, root=5), {})

    def test_basic_structure(self):
        tree = iterative_binary_tree(height=4, root=14)
        self.assertIn("14", tree)
        self.assertEqual(len(tree["14"]), 2)

if __name__ == "__main__":
    unittest.main()
