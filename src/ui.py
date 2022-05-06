import file_acces
from huffman import huffman, dehuffing
from zlw import zlw, un_zlw

class Ui:
    def __init__(self, io) -> None:
        self.io = io

    def start(self):
        self.io.output("welcome to compressing")
        self.options()

    def options(self):
        while True:
            self.io.output("what do you want to do?")
            self.io.output("1: compress with huffman\n2: compress with lzw\n3: compress with both \n4: decompress with huffman\n5: decompress with lzw\n0: quit")
            user_input = self.io.input("")
            if user_input == "1":
                input_file = self.io.input("file to compress: ")
                output_file = self.io.input("where to save: ")
                self.compress_with_huffman(input_file, output_file)
            elif user_input == "2":
                input_file = self.io.input("file to compress: ")
                output_file = self.io.input("where to save: ")
                self.compress_with_lzw(input_file, output_file)
            elif user_input == "3":
                input_file = self.io.input("file to compress: ")
                output_file_huff = self.io.input("where to save huffman: ")
                output_file_lzw = self.io.input("where to save lzw: ")
                self.compress_with_huffman(input_file, output_file_huff)
                self.compress_with_lzw(input_file, output_file_lzw)
            elif user_input == "4":
                input_file = self.io.input("file to decompress: ")
                output_file = self.io.input("where to save: ")
                self.decompress_with_huff(input_file, output_file)
            elif user_input == "5":
                input_file = self.io.input("file to compress: ")
                output_file = self.io.input("where to save: ")
                self.decompress_with_lzw(input_file, output_file)
            else:
                self.io.output("goodbye")
                break

    def compress_with_huffman(self, input_file, output_file):
        self.io.output("compressing...")
        text = file_acces.open_file(input_file)
        compressed_text = huffman(text)
        file_acces.write_bytes(output_file, compressed_text)
        self.io.output("your file has been compressed!")
        original_size = file_acces.get_file_size(input_file)
        new_size = file_acces.get_file_size(output_file)
        self.compare(original_size, new_size)

    def decompress_with_huff(self, input_file, output_file):
        self.io.output("decompressing....")
        bina = file_acces.read_bytes(input_file)
        text = dehuffing(bina)
        file_acces.create_file(output_file, text)
        self.io.output("decompressed!")

    def compress_with_lzw(self, input_file, output_file):
        self.io.output("compressing...")
        text = file_acces.open_file(input_file)
        compressed_text = zlw(text)
        file_acces.write_bytes(output_file, compressed_text)
        self.io.output("your file has been compressed!")
        original_size = file_acces.get_file_size(input_file)
        new_size = file_acces.get_file_size(output_file)
        self.compare(original_size, new_size)

    def decompress_with_lzw(self, input_file, output_file):
        self.io.output("decompressing....")
        bina = file_acces.read_bytes(input_file)
        text = un_zlw(bina)
        file_acces.create_file(output_file, text)
        self.io.output("decompressed!")

    def compare(self, original_size, new_size):
        if original_size == 0:
            self.io.output("original size shouldn't be zero!")
            return
        smaller_prosents = (original_size - new_size)/original_size *100
        self.io.output(f"compressed file is {smaller_prosents}% smaller than the original")
