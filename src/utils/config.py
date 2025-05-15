from dotenv import load_dotenv
import os

load_dotenv() 

NUM_FILES = int(os.getenv("NUM_FILES", "10"))
DIRECTORY = os.getenv("DIRECTORY")
