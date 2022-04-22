import os

def open_file(file_path):
    file = open(file_path, "r")
    content = file.read()
    file.close()
    return content

def create_file(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()

def get_file_size(file_path):
    file_size = os.stat(file_path)
    return file_size.st_size

def read_bytes(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
    file.close()
    hexa = content.hex()
    bina = str("{0:08b}".format(int(hexa, 16)))
    os.remove(file_path)
    return bina

def write_bytes(file_path, content):
    bytes_to_write = bytes(int(content[i : i +8], 2) for i in range(0, len(content), 8))
    with open(file_path, "wb") as bin_file:
        bin_file.write(bytes_to_write)
    bin_file.close()