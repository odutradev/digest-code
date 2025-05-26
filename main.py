import sys
import os

from src.resources.digest_handler import DigestHandler

class InputHandler:
    def __init__(self):
        self.directory = ""

    def prompt(self):
        if len(sys.argv) > 1:
            self.directory = sys.argv[1].strip()
            print(f"Usando diretório: {self.directory}")
        else:
            try:
                self.directory = input("Enter project directory: ").strip()
            except:
                print("\nError in data capture")
                sys.exit(1)
        
        self.validate()

    def validate(self):
        if not os.path.isdir(self.directory):
            print(f"Invalid directory: {self.directory}")
            sys.exit(1)


if __name__ == "__main__":
    handler = InputHandler()
    handler.prompt()
    digest = DigestHandler(handler.directory)
    digest.start()