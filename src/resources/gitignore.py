from src.utils.file import File

import os

class Gitignore:

    def __init__(self, path):
        self.path = path
        self.list = []
    def read_gitignore(self) -> list[str]:
        gitignore_path = os.path.join(self.path, '.gitignore')

        if not File.file_exists(gitignore_path):
            return []

        content = File.read_file(gitignore_path)
        lines = content.splitlines()

        self.lines = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    def is_ignored(self, target: str) -> bool:
        return any(target == pattern or target.startswith(pattern.rstrip('/')) for pattern in self.list)
