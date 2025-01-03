BOOK_PATH = "books//frankenstein.txt"


def count_words(word_str):
    return len(word_str.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    sorted_chars = sorted(chars.items(), key=lambda x:(x[1], x[0]), reverse=1)
    sorted_chars = dict(sorted_chars)
    return sorted_chars

def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()

    chars = get_chars_dict(file_contents)
    word_count = count_words(file_contents)

    # print start of report
    report_text = f"""--- Begin report of {BOOK_PATH} ---
    {word_count} words found in the document"""
    print(report_text)

    #  print info for each char
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")
    print("--- End report ---")

main()