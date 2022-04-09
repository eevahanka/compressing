import heapq
import string
from huffman_tree import create_node, add_node

def huffman(text):
    frequencies = get_frequencies(text)
    nodes = make_nodes_heap(frequencies)
    tree = make_tree(nodes)
    codes = calculate_codes(tree)
    binary_for_huffman = make_huffman(codes, text)
    return get_everything_in_bin(binary_for_huffman, tree)

def get_frequencies(text):
    frequencies = {}
    letters = string.printable
    for letter in letters:
        frequencies[letter] = 0
    for letter in text:
        frequencies[letter] += 1
    return frequencies

def make_nodes_heap(frequencies):
    nodes = []
    for symbol, value in frequencies.items():
        if value != 0:
            node = create_node(value, symbol)
            nodes.append((value, node))
    heapq.heapify(nodes)
    return nodes

def make_tree(nodes):
    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)[1]
        node2 = heapq.heappop(nodes)[1]
        new_node = add_node(node1, node2)
        heapq.heappush(nodes, (new_node.value, new_node))
    return heapq.heappop(nodes)[1]

def calculate_codes(point, codes={}, code=""):
    if point.left_child:
        code0 = code + "0"
        codes = calculate_codes(point.left_child, codes, code0)
    if point.right_child:
        code1 = code + "1"
        codes = calculate_codes(point.right_child, codes, code1)
    if point.symbol:
        codes[point.symbol] = code
    return codes

def make_huffman(codes, text):
    binary_for_huffman = ""
    for symbol in text:
        binary_for_huffman += codes[symbol]
    return binary_for_huffman

def get_everything_in_bin(binary_form, tree):
    tree_in_binary = tree_to_binary(tree)
    tree_lenght_bin = format(len(tree_in_binary), "016b")
    data_lenght_bin = format(len(binary_form), "016b")
    #lenght of tree in bin, lenght of the data in bin, tree in bin, data in bin, couple extra bits
    over_from_bytes = (32 + len(tree_in_binary) + len(binary_form)) % 8
    extra_bits_needed = 8 - over_from_bytes
    extra_bits = "0" * extra_bits_needed
    to_save = tree_lenght_bin + data_lenght_bin + tree_in_binary + binary_form + extra_bits
    return to_save

def tree_to_binary(tree, tree_in_binary=""):
    # 0 for leaf, 1 has children, left 1st right 2nd
    if tree.symbol:
        tree_in_binary += "1"
        symbol_in_ascii = ord(tree.symbol)
        symbol_in_binary = format(symbol_in_ascii, '07b')
        tree_in_binary += symbol_in_binary
    else:
        tree_in_binary += "0"
        tree_in_binary = tree_to_binary(tree.left_child, tree_in_binary)
        tree_in_binary = tree_to_binary(tree.right_child, tree_in_binary)
    return tree_in_binary

#dehuffing
