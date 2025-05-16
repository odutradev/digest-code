# Digest Code

A simple Python tool to extract every text-based file from a project and bundle its contents into a single .txt for AI review and analysis.

**Repository:** [https://github.com/odutradev/digest-code](https://github.com/odutradev/digest-code)
**Creator & Main Contributor:** [João Dutra (@odutradev)](https://github.com/odutradev)


## 🚀 Key Features

* **Recursive directory scan** for all text-based files
* **Respects `.gitignore`** plus default ignore patterns (e.g., `__pycache__/`, `node_modules/`)
* **Filters** by common text extensions: `.py`, `.js`, `.md`, `.json`, `.env`, etc.
* **Interactive prompt** to enter project directory
* **Aggregated output** with `STARTOFFILE <path>` / `ENDOFFILE <path>` blocks
* **Single output file** named after the project root, saved in the `result/` folder


## 💾 Installation

```bash
# Clone the repository
git clone https://github.com/odutradev/digest-code.git
cd digest-code

# Install dependencies
pip install -r requirements.txt
```


## 🎬 Usage

For development, run the main module:

```bash
python -m main
```

Follow the on-screen prompt to enter your project directory. The script will:

1. Recursively scan the specified directory.
2. Filter out non-text files and apply ignore rules.
3. Wrap each file's content in `STARTOFFILE <relative_path>` / `ENDOFFILE <relative_path>` blocks.
4. Save the aggregated output to:

```
result/<project_folder_name>.txt
```


## 📂 Project Structure

```
.
├── main.py              # Entry point and input handler
├── .env.example         # Example environment file (optional)
├── requirements.txt     # Python dependencies
└── src
    ├── resources
    │   ├── digest_handler.py  # Core scanning and bundling logic
    │   └── gitignore.py       # .gitignore parser and default ignore patterns
    └── utils
        ├── config.py         # Loads DIRECTORY from .env for development
        └── file.py           # Helpers for file existence and reading
```


## 🔍 Example Output

After running:

```bash
python -m main
```

The `result/` folder will contain:

```
result/
└── my-project.txt
```

Inside `my-project.txt`:

```text
STARTOFFILE src/app.py

<file contents>

ENDOFFILE src/app.py

STARTOFFILE src/utils/helper.py

<file contents>

ENDOFFILE src/utils/helper.py
...
```


## 🛠️ Customization

* **Extensions**: Update the `TEXT_EXTENSIONS` set in `src/resources/digest_handler.py`
* **Ignore patterns**: Modify default patterns in `src/resources/gitignore.py`
* **Output folder**: Change the `result_dir` path in `DigestHandler.create_file()`


## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "feat: Add YourFeature"`
4. Push to your branch: `git push origin feature/YourFeature`
5. Open a Pull Request

Please read [CONTRIBUTING.md](https://github.com/odutradev/digest-code/blob/master/CONTRIBUTING.md) for contribution guidelines.


## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](https://github.com/odutradev/digest-code/blob/master/LICENSE) for details.
