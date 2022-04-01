import unittest
import huffman

class TestHuffman(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_frequencies(self):
        text1 = "aabbcc"
        text2 = "abc12.&ada"
        dict1 = huffman.get_frequencies(text1)
        dict2 = huffman.get_frequencies(text2)
        self.assertEqual(dict1["a"], 2)
        self.assertEqual(dict1["b"], 2)
        self.assertEqual(dict1["c"], 2)
        self.assertEqual(dict1["2"], 0)
        self.assertEqual(dict2["a"], 3)
        self.assertEqual(dict2["b"], 1)
        self.assertEqual(dict2["c"], 1)
        self.assertEqual(dict2["1"], 1)
        self.assertEqual(dict2["2"], 1)
        self.assertEqual(dict2["."], 1)
        self.assertEqual(dict2["&"], 1)







