import unittest
from searching.depth_first import DepthFirst

class TestDepthFirst(unittest.TestCase):
    def setUp(self):
        self.dfs = DepthFirst()

    def test_dfs_simple_graph(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1, 3, 4, 2])

    def test_dfs_disconnected_graph(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1, 2])

    def test_dfs_single_node(self):
        graph = {1: []}
        result = self.dfs.search(graph, 1)
        self.assertEqual(result, [1])

if __name__ == "__main__":
    unittest.main()
