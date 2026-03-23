with open('dataset.txt', 'r') as f:
    text = f.read()
    paragraphs = text.split("\n\n")
    tokens = [token for paragraph in paragraphs for token in paragraph.split()]
    print(tokens)