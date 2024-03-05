def read_file(path):
    with open(path, "r") as f:
        return f.read()


def get_word_count(corpus):
    return len(corpus.split())


def main():
    file_contents = read_file("books/frankenstein.txt")
    print(get_word_count(file_contents))


if __name__ == "__main__":
    main()
