def space_tokenizer(file_path: str = "dataset.txt"):
    with open(file_path, 'r') as f:
        text = f.read()
        paragraphs = text.split("\n\n")
        tokens = [token for paragraph in paragraphs for token in paragraph.split()]

    return tokens

if __name__ == "__main__":
    print(space_tokenizer())