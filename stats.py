def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_word_counts(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)