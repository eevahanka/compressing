import os

def open_file(file_path):
    f = open(file_path, "r")
    content = f.read()
    f.close()
    return content

def create_file(file_path, content):
    f = open(file_path, "w")
    f.write(content)
    f.close()

def get_file_size(file_path):
    #bytes!
    file_size = os.stat(file_path)
    return file_size.st_size


