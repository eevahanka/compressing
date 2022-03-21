import io


class Ui:
    def __init__(self, io) -> None:
        self.io = io

    def start(self):
        self.io.output("welcome to compressing")
        