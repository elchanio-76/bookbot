from stats import count_words, count_characters, sort_word_counts, chars_dict_to_sorted_list
import sys
import os

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        # book_path="./books/frankenstein.txt"
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
        
    if not os.path.exists(book_path):
        print(f"Error: The file {book_path} does not exist.")
        sys.exit(1)

    text = get_book_text(book_path)
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    
    # These lines were added to print the character counts for an earlier submission
    # sorted_chars = chars_dict_to_sorted_list(char_counts)
    # for item in sorted_chars:
    #     print(item)
    
    print("--------- Character Count -------")
    sorted = sort_word_counts(char_counts)
    for char, count in sorted:
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
