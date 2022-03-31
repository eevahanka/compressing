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
    #bytes!
    file_size = os.stat(file_path)
    return file_size.st_size
