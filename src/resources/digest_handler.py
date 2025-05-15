import os

from src.utils.config import DIRECTORY, NUM_FILES
from src.resources.gitignore import Gitignore
from src.utils.file import File

class DigestHandler:
    def __init__(self, num_files, directory):
        self.released_files: list[dict[str, str]] = []
        self.directory = directory
        self.num_files = num_files
        self.finish_text = ""

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

        self.create_file()

    def create_file(self):
        for item in self.released_files:
            path = item["relative_path"]
            print(f"Performing file processing: {path}")
            file_content = File.read_file(item["full_path"])
            self.finish_text += f"STARTOFFILE {path}\n\n{file_content}\n\nENDOFFILE {path}\n\n"

        result_dir = os.path.join(self.directory, "result")
        os.makedirs(result_dir, exist_ok=True)

        output_path = os.path.join(result_dir, "output.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(self.finish_text)

        print(f"Arquivo gerado em: {output_path}")

if __name__ == "__main__":
    handler = DigestHandler(NUM_FILES, DIRECTORY)
    print(NUM_FILES, DIRECTORY)
    handler.start()