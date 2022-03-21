import io

class Ui:
    def __init__(self, io) -> None:
        self.io = io

    def start(self):
        self.io.output("welcome to compressing")
        file_to_compress = self.get_file()
        self.compressing(file_to_compress)

    def get_file(self):
        #this is temporary 
        file_to_compress = self.io.input("what do you want to compress? ")
        return file_to_compress

    def compressing(self, file_to_compress):
        self.io.output("compressing...")
        #will call compressing algorthims !
        self.io.output("this feature doesn't exist!")