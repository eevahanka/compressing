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

class TestMain(unittest.TestCase):
    def setup(self):
        self.io = Stub_io()
        self.stub_ui = Ui(self.io)



