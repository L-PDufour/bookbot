def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict)

def print_report(chars_dict):
    filtered_chars = {char: count for char, count in chars_dict.items() if char.isalpha()}

    sorted_chars = sorted(filtered_chars.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
