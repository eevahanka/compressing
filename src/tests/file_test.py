import unittest
import file_acces

class TestFile_acces(unittest.TestCase):
    def setUp(self):
        self.file_path = "src/tests/test_file.txt"
        self.content = "i am a a very important file for the tests. So please do not edit me!"
        self.size = 69


    def test_gets_correct_content(self):
        
        on_file = file_acces.open_file(self.file_path)
        self.assertEqual(self.content, on_file)

    def test_writes_correctly(self):
        file_acces.create_file(self.file_path, self.content)
        on_file = file_acces.open_file(self.file_path)
        self.assertEqual(self.content, on_file)

    def test_tells_correct_size(self):
        file_size = file_acces.get_file_size(self.file_path)
        self.assertEqual(self.size, file_size)


