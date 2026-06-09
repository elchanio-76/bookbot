def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_word_counts(word_counts: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

def sort_on(char_counts: tuple[str,int])->int:
    return char_counts[1]

def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str,int]]:
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append((ch, num_chars_dict[ch]))
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

