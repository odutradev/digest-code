import os

from src.utils.config import DIRECTORY, NUM_FILES
from src.resources.gitignore import Gitignore
from src.utils.file import File

class DigestHandler:
    def __init__(self, num_files, directory):
        self.directory = directory
        self.num_files = num_files
        self.released_files: list[dict[str, str]] = []

    def start(self):
        print(f"Processing up to {self.num_files} files in {self.directory}")

        gitignore_validation = Gitignore(self.directory)
        gitignore_validation.read_gitignore()

        for root, dirs, files in os.walk(self.directory):
            dirs[:] = [
                d for d in dirs
                if not gitignore_validation.is_ignored(
                    os.path.relpath(os.path.join(root, d), start=self.directory).replace(os.sep, "/")
                )
            ]

            for file in files:
                full_path = os.path.join(root, file)
                if not File.file_exists(full_path):
                    continue

                relative_path = os.path.relpath(full_path, start=self.directory).replace(os.sep, "/")
                is_ignored = gitignore_validation.is_ignored(relative_path)

                if not is_ignored:
                    self.released_files.append({
                        "relative_path": relative_path,
                        "full_path": full_path
                    })

        for item in self.released_files:
            print(item)

if __name__ == "__main__":
    handler = DigestHandler(NUM_FILES, DIRECTORY)
    print(NUM_FILES, DIRECTORY)
    handler.start()