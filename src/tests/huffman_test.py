import unittest
import huffman
import heapq

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.freq_dict = {"a": 4, "n": 1, "b": 0, "4": 2}

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

    def test_heap_creation(self):
        nodes_heap = huffman.make_nodes_heap(self.freq_dict)
        self.assertEqual(len(nodes_heap), 3)
        node = heapq.heappop(nodes_heap)
        self.assertEqual(node.symbol, "n")
        self.assertEqual(node.value, 1)
        heapq.heappop(nodes_heap)
        node = heapq.heappop(nodes_heap)
        self.assertEqual(node.symbol, "a")
        self.assertEqual(node.value, 4)

    def test_tree_creation(self):
        nodes_heap = huffman.make_nodes_heap(self.freq_dict)
        node = huffman.make_tree(nodes_heap)
        node1 = node.right_child
        self.assertEqual(node1.symbol, "a")
        self.assertEqual(node1.value, 4)
        self.assertEqual(node1.left_child, None)
        self.assertEqual(node1.right_child, None)
        node2 = node.left_child.right_child
        self.assertEqual(node2.symbol, "4")
        node3 = node.left_child
        self.assertEqual(node3.value, 3)
        self.assertEqual(node3.symbol, None)

    def test_symbols_can_have_same_frequencies(self):
        same_frequencies = {"a": 4, "b": 4}
        nodes_heap  =huffman.make_nodes_heap(same_frequencies)
        tree = huffman.make_tree(nodes_heap)
        self.assertEqual(1,1) #if it makes it here woth out an error it works:D

    def test_calculates_correct_codes(self):
        nodes_heap = huffman.make_nodes_heap(self.freq_dict)
        node = huffman.make_tree(nodes_heap)
        codes = huffman.calculate_codes(node)
        self.assertEqual(codes["n"],"00")
        self.assertEqual(codes["4"],"01")
        self.assertEqual(codes["a"],"1")

    def test_make_huffman(self):
        codes = {'n': '00', '4': '01', 'a': '1'}
        text = "aa4na4"
        binary_for_huffman = huffman.make_huffman(codes, text)
        self.assertEqual(binary_for_huffman, "110100101")
    
    def test_tree_to_binary(self):
        nodes_heap = huffman.make_nodes_heap(self.freq_dict)
        node = huffman.make_tree(nodes_heap)
        tree_in_binary = huffman.tree_to_binary(node)
        self.assertEqual("00111011101011010011100001", tree_in_binary)

    def test_makes_correct_binary(self):
        bin_huff = huffman.huffman("aa4na4")
        self.assertEqual(bin_huff, "00000000000000000000000000011010000000000000000000000000000010010011101110101101001110000111010010100000" )

    def test_get_tree(self):
        tree_in_binary = "00111011101011010011100001"
        tree = huffman.get_tree(tree_in_binary)
        node1 = tree.right_child
        self.assertEqual(node1.symbol, "a")
        self.assertEqual(node1.left_child, None)
        self.assertEqual(node1.right_child, None)
        node2 = tree.left_child.right_child
        self.assertEqual(node2.symbol, "4")
        node3 = tree.left_child
        self.assertEqual(node3.symbol, None)
    
    def test_get_text(self):
        text_in_binary = "110100101"
        tree_in_binary = "00111011101011010011100001"
        tree = huffman.get_tree(tree_in_binary)
        text = huffman.get_text(text_in_binary, tree)
        self.assertEqual(text, "aa4na4")

    def test_huffman_works(self):
        text = "im wery long and comlpvate text eith numbers and other things 12345!!"
        bina = huffman.huffman(text)
        text_after_compressing = huffman.dehuffing(bina)
        self.assertEqual(text, text_after_compressing)
        text = "i am a a very important file for the tests. So please do not edit me!"
        bina = huffman.huffman(text)
        text_after_compressing = huffman.dehuffing(bina)
        self.assertEqual(text, text_after_compressing)


        