import os

from src.resources.gitignore import Gitignore
from src.utils.config import DIRECTORY
from src.utils.file import File

TEXT_EXTENSIONS = {
    ".txt", ".md", ".py", ".js", ".jsx", ".ts", ".tsx",
    ".json", ".html", ".css", ".xml", ".yml", ".yaml",
    ".csv", ".ini", ".env", ".cfg", ".example"
}

class DigestHandler:
    def __init__(self, directory):
        self.released_files: list[dict[str, str]] = []
        self.directory = directory
        self.finish_text = ""

    def is_text_file(self, file_path: str) -> bool:
        _, ext = os.path.splitext(file_path)
        return ext.lower() in TEXT_EXTENSIONS

    def start(self):
        print(f"Processing files from directory {self.directory}")

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

                if not self.is_text_file(full_path):
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

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        result_dir = os.path.join(project_root, "result")
        os.makedirs(result_dir, exist_ok=True)

        base_name = os.path.basename(os.path.normpath(self.directory))
        output_filename = f"{base_name}.txt"
        output_path = os.path.join(result_dir, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(self.finish_text)

        print(f"Arquivo gerado em: {output_path}")

if __name__ == "__main__":
    handler = DigestHandler(DIRECTORY)
    handler.start()
