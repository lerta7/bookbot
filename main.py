BOOK_PATH = "books//frankenstein.txt"

with open(BOOK_PATH) as f:
    file_contents = f.read()

def count_words(word_str):
    return len(word_str.split())

def count_chars(word_str):
    lower_str = word_str.lowercase()

print(count_words(file_contents))