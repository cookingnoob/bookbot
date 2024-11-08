def main():
    try:
        book_path = 'books/frankenstein.txt'
        text = read_file(book_path)
        word_count = total_word_count(text)
        letters = separate_into_letters(text)
        list_of_letters = convert_dictionary_to_list(letters)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{word_count} words found in the document\n")
        for letter in list_of_letters:
            print(f"The '{letter['char']}' character was found {letter['num']} times")
        print("--- End report ---")


    except FileNotFoundError:
        print('file was not found')

def sort_on(dict):
    return dict['num']

def convert_dictionary_to_list(letters):
    list_of_letters = []
    for letter in letters:
        list_of_letters.append({'char' : f'{letter}', 'num': letters[letter]})
    list_of_letters.sort(reverse=True, key=sort_on)
    return list_of_letters

def separate_into_letters(text):
    lower_case = text.lower()
    letter_dictionary = {}
    for word in lower_case:
        for letter in word:
            if letter.isalpha() and letter in letter_dictionary:
                letter_dictionary[letter] += 1
            elif letter.isalpha():
                letter_dictionary[letter] = 1
    return letter_dictionary

def total_word_count(text):
    words = text.split()
    return len(words)


def read_file(book_path):
    with open(book_path) as f:
        return f.read()

main()


    # cwd = Path.cwd()
    # relative_path_books = '/books/frankenstein.txt'

    # f = open(f'{cwd}{relative_path_books}', "r")

    # print(f.read())