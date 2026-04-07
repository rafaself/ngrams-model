from collections import defaultdict, Counter
from typing import List, Tuple

ngram_counts = defaultdict(Counter)

with open("dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

paragraphs = text.split("\n\n")

def space_tokenizer(paragraph: str) -> List[str]:
    return paragraph.split()

tokens = [token for paragraph in paragraphs for token in space_tokenizer(paragraph)]

def generate_ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

ngrams = generate_ngrams(tokens, 3)

for ngram in ngrams:
    context = ngram[:-1]
    token = ngram[-1]
    ngram_counts[context][token] += 1

ngram_counts_result = {
    " ".join(context): dict(counter)
    for context, counter in ngram_counts.items()
}

print(ngram_counts_result)

# Print as table with pandas
import pandas as pd
df = pd.DataFrame(ngram_counts_result)
print(df)