import sys;
import os;

class InputHandler:
    def __init__(self):
        self.directory = ""
        self.numFiles = 0

    def prompt(self):
        self.directory = input("Enter project directory: ").strip()
        try:
            self.numFiles = int(input("Enter number of files to process: ").strip())
        except ValueError:
            print("Invalid number of files")
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
    print(f"Processing up to {handler.numFiles} files in {handler.directory}")
