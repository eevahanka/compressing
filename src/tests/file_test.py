import unittest
import file_acces

class TestFile_acces(unittest.TestCase):
    def setUp(self):
        self.file_path = "src/tests/test_file.txt"
        self.content = "i am a a very important file for the tests. So please do not edit me!"
        self.size = 69
        self.byte_path = "src/tests/test_byte_file.txt"
        file_acces.create_file(self.file_path, self.content)

    def test_gets_correct_content(self):
        on_file = file_acces.open_file(self.file_path)
        self.assertEqual(self.content, on_file)

    def test_writes_correctly(self):
        file_acces.create_file(self.file_path, self.content)
        on_file = file_acces.open_file(self.file_path)
        self.assertEqual(self.content, on_file)
        file_acces.create_file(self.file_path, "")
        on_file = file_acces.open_file(self.file_path)
        self.assertEqual("", on_file)
        file_acces.create_file(self.file_path, self.content)

    def test_tells_correct_size(self):
        file_size = file_acces.get_file_size(self.file_path)
        self.assertEqual(self.size, file_size)

    def test_binary_file(self):
        bina = "000000001001111001110000110011001111000011001100"
        file_acces.write_bytes(self.byte_path, bina)
        on_file = file_acces.read_bytes(self.byte_path)
        self.assertEqual(bina, on_file)
        bina = "0000000000000000000001100001000001100010000001100011000100000001000001100001000001100100"
        file_acces.write_bytes(self.byte_path, bina)
        on_file = file_acces.read_bytes(self.byte_path)
        self.assertEqual(bina, on_file)
