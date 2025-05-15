class DigestHandler:
    def __init__(self, numFiles, directory):
        self.directory = directory
        self.numFiles = numFiles

    def start(self):
         print(f"Processing up to {self.numFiles} files in {self.directory}")
        
if __name__ == "__main__":
    handler = DigestHandler()
    handler.start()