import os 

from src.utils.config import DIRECTORY, NUM_FILES
from src.resources.gitignore import Gitignore
from src.utils.file import File

class DigestHandler:
    def __init__(self, num_files, directory):
        self.directory = directory
        self.num_files = num_files
        self.released_files = []

    def start(self):
        print(f"Processing up to {self.num_files} files in {self.directory}")

        gitignore_validation = Gitignore(self.directory)
        gitignore_validation.read_gitignore()

        for root, _, files in os.walk(self.directory):
            for file in files:
                full_path = os.path.join(root, file)
                hasFile = File.file_exists(full_path)
                if not hasFile: return

                relative_path = os.path.relpath(full_path, start=self.directory)
                is_ignored = gitignore_validation.is_ignored(relative_path)


                print(relative_path, is_ignored)


                



if __name__ == "__main__":
    handler = DigestHandler(NUM_FILES, DIRECTORY)
    print(NUM_FILES, DIRECTORY)
    handler.start()