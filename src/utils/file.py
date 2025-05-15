import os

class File:
    @staticmethod
    def file_exists(path: str) -> bool:
        return os.path.exists(path) and os.path.isfile(path)

    @staticmethod
    def read_file(path: str) -> str:
        if not File.file_exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
