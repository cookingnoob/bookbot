def main():
    try:
        book_path = 'books/frankenstein.txt'
        text = read_file(book_path)
        word_count = total_word_count(text)
        print(f"{word_count} words found in the document")
        letters = separate_into_letters(text)
        print(letters)

    except FileNotFoundError:
        print('file was not found')

def separate_into_letters(text):
    lower_case = all_letters_lowercase(text)
    letter_dictionary = {}
    for word in lower_case:
        for letter in word:
            if letter.isalpha() and letter in letter_dictionary:
                letter_dictionary[letter] += 1
            elif letter.isalpha():
                letter_dictionary[letter] = 1
    return sorted(letter_dictionary.items(), key=lambda x:x[1], reverse=True)

def all_letters_lowercase(text):
    return text.lower()

def total_word_count(text):
    words = separate_into_words(text)
    return len(words)

def separate_into_words(text):
    return text.split()

def read_file(book_path):
    with open(book_path) as f:
        return f.read()

main()


    # cwd = Path.cwd()
    # relative_path_books = '/books/frankenstein.txt'

    # f = open(f'{cwd}{relative_path_books}', "r")

    # print(f.read())