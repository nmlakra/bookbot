def read_file(path):
    with open(path, "r") as f:
        return f.read()


def get_word_count(corpus):
    return len(corpus.split())


def get_char_counts(corpus):
    counter = {}
    for char in corpus:
        char = char.lower()
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    return counter


def is_letter(char):
    return char.isalpha()


def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_file(book_path)
    word_count = get_word_count(file_contents)
    char_counts = get_char_counts(file_contents)

    letter_counts = sorted(
        filter(lambda x: is_letter(x[0]), char_counts.items()),
        key=lambda x: x[1],
        reverse=True,
    )

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document\n")
    for letter, count in letter_counts:
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
