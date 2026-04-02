# N-grams Model

This project implements a simple n-grams language model based on a given dataset.

## Features

- **Tokenization**: Splits text into tokens (words).
- **N-gram Generation**: Creates n-grams (sequences of n tokens) from the token list.
- **Frequency Counting**: Counts the occurrences of each n-gram.
- **Context-based Prediction**: Predicts the next token based on the preceding context.

## Usage

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Model**:
    ```bash
    python token_presumer.py
    ```

## Dataset

The model is trained on the `dataset.txt` file.

## Output

The script generates a dictionary where keys are the context (n-1 tokens) and values are dictionaries of the next token and its frequency count.

Example output structure:

```json
{
  "context words": {
    "next_word_1": count_1,
    "next_word_2": count_2
  }
}
```
