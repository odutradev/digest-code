# Digest Code

A simple Python tool to extract every text-based file from a project and bundle its contents into a single `.txt` for AI review and analysis.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Example Output](#example-output)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **Recursive scan** of project directories  
- **Filtering** by common text extensions (`.py`, `.js`, `.md`, etc.)  
- Honors `.gitignore` (plus default ignores like `node_modules/` and `__pycache__/`)  
- **Limit** number of files processed (configurable)  
- Preserves **relative paths** inside output blocks  
- Generates a single aggregate file with `STARTOFFILE` / `ENDOFFILE` delimiters  

---

## Prerequisites

- Python 3.8 or higher  
- pip  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/odutradev/digest-code.git
   cd digest-code


2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Create a `.env` file in the project root (next to `requirements.txt`) to set defaults:

```dotenv
# .env
DIRECTORY=/path/to/your/project
NUM_FILES=50
```

* `DIRECTORY`: default root folder to scan
* `NUM_FILES`: maximum number of files to include

If you omit the `.env` file, the defaults are:

* `NUM_FILES`: 10
* `DIRECTORY`: (empty – prompts at runtime)

---

## Usage

You can run interactively or rely on `.env` defaults:

```bash
# Interactive prompt
python main.py
```

You will be asked:

1. **Enter project directory**
2. **Enter number of files to process**

Once confirmed, the tool will:

* Walk your directory tree
* Filter out non-text files and ignored paths
* Collect up to `NUM_FILES` text files
* Write all contents into `./result/<project_name>.txt`

---

## Project Structure

```
.
├── main.py
├── README.md
├── requirements.txt
├── .env.example
└── src
    ├── resources
    │   ├── digest_handler.py   # core logic
    │   └── gitignore.py        # .gitignore parsing
    └── utils
        ├── config.py           # loads .env
        └── file.py             # file read/existence helpers
```

---

## Example Output

After running:

```bash
python -m main.py
```

You’ll find:

```
result/
└── my-project.txt
```

Its contents look like:

```
STARTOFFILE src/app.py

<file contents here>

ENDOFFILE src/app.py

STARTOFFILE src/utils/helper.py

<file contents here>

ENDOFFILE src/utils/helper.py
...
```

---

## Customization

* **Extensions**: Modify `TEXT_EXTENSIONS` in `src/resources/digest_handler.py`
* **Ignore patterns**: Add defaults in `src/resources/gitignore.py`
* **Output folder**: Change `result` path in `DigestHandler.create_file()`

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "feat: Add YourFeature"`
4. Push to your branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

