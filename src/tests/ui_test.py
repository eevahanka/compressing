import unittest
from ui import Ui

class Stub_io:
    def __init__(self, inputs = []) -> None:
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
