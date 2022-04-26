import unittest
import zlw

class TestZlw(unittest.TestCase):
    def setUp(self):
        pass

    def test_compress(self):
        text = "abcbcad"
        compressed_list = zlw.compress_zlw(text)
        self.assertEqual(compressed_list, [97, 98, 99, 257, 97, 100]) #"97989925797100"
        text = "aboatdboaxboaboa"
        compressed_list = zlw.compress_zlw(text)
        self.assertEqual(compressed_list, [97, 98, 111, 97, 116, 100, 257, 97, 120, 262, 262]) #"97981119711610025797120262262"

    def test_uncompress(self):
        compressed_list = [97, 98, 99, 257, 97, 100]
        text = zlw.un_compress_zlw(compressed_list)
        self.assertEqual(text, "abcbcad")
        compressed_list = [97, 98, 111, 97, 116, 100, 257, 97, 120, 262, 262]
        text = zlw.un_compress_zlw(compressed_list)
        self.assertEqual(text, "aboatdboaxboaboa")

    def test_make_zlw_binary(self):
        compressed_list = [97, 98, 99, 257, 97, 100]
        compressed_binary = zlw.make_zlw_binary(compressed_list)
        self.assertEqual(compressed_binary, "00000000000001100001000001100010000001100011000100000001000001100001000001100100")
        compressed_list = [97, 98, 99, 257, 97]
        compressed_binary = zlw.make_zlw_binary(compressed_list)
        self.assertEqual(compressed_binary, "000001000000000001100001000001100010000001100011000100000001000001100001")

    def test_get_binary(self):
        compressed_binary = "00000000000001100001000001100010000001100011000100000001000001100001000001100100"
        compressed_list = zlw.get_compressed_list_from_binary(compressed_binary)
        self.assertEqual(compressed_list, [97, 98, 99, 257, 97, 100])

    def test_zlw_works(self):
        text = "abcbcad"
        compressed_binary = zlw.zlw(text)
        self.assertEqual(compressed_binary, "00000000000001100001000001100010000001100011000100000001000001100001000001100100")

    def test_un_zlw_woks(self):
        compressed_binary = "00000000000001100001000001100010000001100011000100000001000001100001000001100100"
        text = zlw.un_zlw(compressed_binary)
        self.assertEqual(text, "abcbcad")