import functools
import json
import os
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Your existing functions
def fix_token_wise_length(strs: list, tokenizer, max_size: int = 728, min_size: int = 25) -> list:
    out_list = []
    tmp = ""
    s_size = 0
    last_s_size = 0
    for i, s in enumerate(strs):
        cleansed_s = s.lstrip().rstrip()
        tmp = tmp + cleansed_s
        s_size += len(tokenizer.tokenize(cleansed_s))
        if s_size < min_size:
            if i > 0 and (last_s_size + s_size <= max_size):
                out_list[-1] += "\n" + tmp
                last_s_size += s_size
                tmp = ""
                s_size = 0
            else:
                tmp += "\n"
        else:
            out_list.append(tmp)
            last_s_size = s_size
            tmp = ""
            s_size = 0
    return out_list


@functools.lru_cache()
def get_tokenizer(model_name):
    return SentenceTransformer(model_name).tokenizer


def chunk_text(
        in_txt: str,
        splitter=None,
        tokenizer=None,
        max_chunk_size: int = 728,
        chunk_overlap: int = 50,
        adjust_chunk_size: bool = True,
        min_chunk_size: int = 50
) -> list:
    if tokenizer is None and (splitter is None or adjust_chunk_size):
        model_name = "sentence-transformers/distiluse-base-multilingual-cased-v2"
        tokenizer = get_tokenizer(model_name)
    if splitter is None:
        splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
            tokenizer,
            chunk_size=max_chunk_size,
            chunk_overlap=chunk_overlap
        )
    chunks = splitter.split_text(in_txt)
    if adjust_chunk_size:
        chunks = fix_token_wise_length(
            chunks,
            tokenizer,
            max_chunk_size,
            min_chunk_size
        )
    return chunks


# New functions for handling JSON files


def process_json_file(input_file, output_file, key="content"):
    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    text = json_data[key]

    chunks = chunk_text(text)

    json_data["CHUNK__"] = chunks

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False)


def process_json_files_in_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)
            process_json_file(input_file_path, output_file_path)


if __name__ == "__main__":
    input_directory = "file-path"
    output_directory = "file-path"

    process_json_files_in_directory(input_directory, output_directory)
