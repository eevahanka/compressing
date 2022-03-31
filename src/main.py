from ui import Ui
from io_for_ui import Io

def main():
    io = Io()
    ui = Ui(io)
    ui.start()

if __name__ == "__main__":
    main()
