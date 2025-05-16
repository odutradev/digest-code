import pathspec
import os

from src.utils.file import File

class Gitignore:
    def __init__(self, path: str):
        self.spec = pathspec.PathSpec.from_lines('gitwildmatch', [])
        self.path = path

    def read_gitignore(self) -> list[str]:
        gitignore_path = os.path.join(self.path, '.gitignore')

        patterns = []

        if File.file_exists(gitignore_path):
            content = File.read_file(gitignore_path)
            patterns = content.splitlines()

        patterns += [
            '.git',
            '**/__pycache__/',
            '**/node_modules/',
            'package-lock.json'
        ]

        self.spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)
        return [p.pattern for p in self.spec.patterns]

    def is_ignored(self, target: str) -> bool:
        return self.spec.match_file(target)
