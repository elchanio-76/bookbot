from stats import count_words, count_characters, sort_word_counts
import sys

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    print("--------- Character Count -------")
    sorted = sort_word_counts(char_counts)
    for char, count in sorted:
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
