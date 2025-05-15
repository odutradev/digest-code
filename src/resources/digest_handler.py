from src.utils.config import DIRECTORY, NUM_FILES

class DigestHandler:
    def __init__(self, num_files, directory):
        self.directory = directory
        self.num_files = num_files

    def start(self):
        print(f"Processing up to {self.num_files} files in {self.directory}")

if __name__ == "__main__":
    handler = DigestHandler(NUM_FILES, DIRECTORY)
    print(NUM_FILES, DIRECTORY)
    handler.start()