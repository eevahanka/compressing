import unittest
from ui import Ui

class Stub_io:
    def __init__(self, inputs=[]) -> None:
        self.inputs = inputs
        self.outputs = []

    def input(self, input_name):
        return self.inputs.pop(0)

    def output(self, user_output):
        self.outputs.append(user_output)

class TestUi(unittest.TestCase):
    def setUp(self):
        self.io = Stub_io()
        self.stub_ui = Ui(self.io)

    def test_compare_calculates_correctly(self):
        self.stub_ui.compare(10, 4)
        self.assertEqual(f"compressed file is 60.0% smaller than the original", self.io.outputs[-1])

    def test_compare_dosent_divide_by_zero(self):
        self.stub_ui.compare(0, 4)
        self.assertEqual("original size shouldn't be zero!", self.io.outputs[-1])

    def test_compress_with_huffman(self):
        file_path = "src/tests/test_file.txt"
        byte_path = "src/tests/test_byte_file.txt"
        self.io = Stub_io(["1", file_path, byte_path, "4", byte_path, file_path, "0"])
        self.stub_ui = Ui(self.io)
        self.stub_ui.start()
        self.assertEqual("goodbye", self.io.outputs[-1])

    def test_compress_with_zlw(self):
        file_path = "src/tests/test_file.txt"
        byte_path = "src/tests/test_byte_file.txt"
        self.io = Stub_io(["2", file_path, byte_path, "5", byte_path, file_path, "0"])
        self.stub_ui = Ui(self.io)
        self.stub_ui.start()
        self.assertEqual("goodbye", self.io.outputs[-1])