import unittest

class Stub_io:
    def __init__(self, inputs = []) -> None:
        self.inputs = inputs
        self.outputs = []

    def input(self, input_name):
        return self.inputs.pop(0)

    def output(self, user_output):
        self.outputs.append(user_output)

class TestMain(unittest.TestCase):
    def setup(self):
        pass

    def test_is_working(self):
        self.assertEqual(0, 0)
