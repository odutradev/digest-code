import os
from src.utils.file import File
import pathspec

class Gitignore:
    def __init__(self, path: str):
        self.path = path
        self.spec = pathspec.PathSpec.from_lines('gitwildmatch', [])

    def read_gitignore(self) -> list[str]:
        gitignore_path = os.path.join(self.path, '.gitignore')

        if File.file_exists(gitignore_path):
            content = File.read_file(gitignore_path)
            lines = content.splitlines()
            self.spec = pathspec.PathSpec.from_lines('gitwildmatch', lines)

        self.spec = pathspec.PathSpec.from_lines(
            'gitwildmatch',
            list(self.spec.patterns) + ['.git']
        )

        return [p.pattern for p in self.spec.patterns]

    def is_ignored(self, target: str) -> bool:
        return self.spec.match_file(target)
