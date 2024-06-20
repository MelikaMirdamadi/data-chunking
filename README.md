

---

# JSON Chunking and Tokenization Tool

This Python script processes JSON files by splitting the text content into chunks, ensuring each chunk meets specified token length requirements. The tool is designed to handle nested JSON structures and can process multiple files within a directory.

## Features

- Splits text content in JSON files into manageable chunks.
- Ensures chunks meet specified token length requirements.
- Handles nested JSON structures.
- Processes multiple JSON files in a directory.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MelikaMirdamadi/data-chunking.git
   cd json-chunking-tool
   ```

2. **Set up a Python virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install sentence-transformers langchain
   ```

## Usage

1. **Prepare your input directory:**

   Ensure you have an input directory named `input-file-path` containing JSON files with the key `"content"` holding the text you want to process.

2. **Run the script:**

   Execute the script using Python:

   ```bash
   python main.py
   ```

3. **Output:**

   The processed JSON files with added chunks will be saved in the specified output directory (`output-file-path`).

## Code Overview

### Main Functions

- `fix_token_wise_length`: Adjusts the size of text chunks based on token length.
- `get_tokenizer`: Retrieves the tokenizer for the specified model.
- `chunk_text`: Splits text into chunks using the specified tokenizer and splitter.
- `process_json_file`: Processes a single JSON file, adding text chunks to the JSON data.
- `process_json_files_in_directory`: Processes all JSON files in a directory.

### Example

Given an input JSON file (`input-file-path/example.json`):

```json
{
    "content": "This is some sample text content that will be split into chunks."
}
```

After running the script, the output JSON file (`output-file-path/example.json`) will include the processed chunks:

```json
{
    "content": "This is some sample text content that will be split into chunks.",
    "CHUNK__": [
        "This is some sample text content that",
        "will be split into chunks."
    ]
}
```

## Customization

- **Adjusting Chunk Sizes:** Modify the `max_chunk_size`, `chunk_overlap`, and `min_chunk_size` parameters in the `chunk_text` function to customize chunking behavior.
- **Changing Input/Output Paths:** Update the `input_directory` and `output_directory` variables in the `__main__` block to specify different directories.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---



