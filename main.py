def main():
    path_to_file = "books/frankenstein.txt"
    text = open_file(path_to_file)
    number_of_words = count_words(text)
    number_of_char = number_of_appearance(text)

    display_report(number_of_words, number_of_char)

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def open_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def number_of_appearance(text):
    char_dict = {}
    for word in text:
        if word.lower() not in char_dict:
            char_dict[word.lower()] = 1
        else:
            char_dict[word.lower()] += 1

    return char_dict

def display_report(word_count, char_dict):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_set = set()
    for letter in alphabet:
        alphabet_set.add(letter)
    
    header = f"""--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n"""
    footer = """
    \n--- End report ---
    """
    body = ""
    for char in char_dict:
        if char in alphabet_set:
            body += f"\nThe '{char}' character was found {char_dict[char]} times"

    final_report = header + body + footer

    print(final_report)

main()