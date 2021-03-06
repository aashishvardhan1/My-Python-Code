class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already Closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")