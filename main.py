import sys;
import os;

from src.resources.digest_handler import DigestHandler

class InputHandler:
    def __init__(self):
        self.directory = ""
        self.numFiles = 0

    def prompt(self):
        try:
            self.directory = input("Enter project directory: ").strip()
            self.numFiles = int(input("Enter number of files to process: ").strip())
        except:
            print("\nError in data capture")
            sys.exit(1)
        self.validate()

    def validate(self):
        if not os.path.isdir(self.directory):
            print(f"Invalid directory: {self.directory}")
            sys.exit(1)
        if self.numFiles <= 0:
            print("Number of files must be greater than zero")
            sys.exit(1)

if __name__ == "__main__":
    handler = InputHandler()
    handler.prompt()
    digest = DigestHandler(handler.numFiles, handler.directory)
    digest.start()

