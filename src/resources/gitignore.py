import os
from src.utils.file import File

class Gitignore:
    def __init__(self, path: str):
        self.path = path
        self.patterns: list[str] = []

    def read_gitignore(self) -> list[str]:
        gitignore_path = os.path.join(self.path, '.gitignore')

        if File.file_exists(gitignore_path):
            content = File.read_file(gitignore_path)
            lines = content.splitlines()
            self.patterns = [
                line.strip()
                for line in lines
                if line.strip() and not line.startswith('#')
            ]

        if ".git" not in self.patterns:
            self.patterns.append(".git")

        return self.patterns

    def is_ignored(self, target: str) -> bool:
        return any(
            target == pattern or target.startswith(pattern.rstrip('/'))
            for pattern in self.patterns
        )
