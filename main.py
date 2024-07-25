def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    letter_counter = count_letters(text)
    if text:
        counter = get_words(text)
    else:
        counter = 'Error: could not read the book'
    ordered_letters = order(letter_counter)
    print('--- Begin report of books/frankenstein.txt ---')
    print(len(counter), 'words found in the document \n')
    for letter in ordered_letters:

        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print('--- End report ---')

#sorts the letters with the count key
def higher_count(e):
    return e['count']

#recived the counted letters dictionary and adds letter and count keys so .sort() can be used
def order(letters):
    letter_list = [{'letter': k, 'count': v}for k,v in letters.items()]
    letter_list.sort(reverse=True,key=higher_count)
    return letter_list
   
#separates the whole text into a list of strings
def get_words(text):
    if(len(text) == 0):
        return 'Could not count how many words the book has'
    words = text.split()
    return words


def count_letters(text):
    alphabet= {
              'a': 0,
              'b': 0,
              'c': 0,
              'd': 0,
              'e': 0,
              'f': 0,
              'g': 0,
              'h': 0,
              'i': 0,
              'j': 0,
              'k': 0,
              'l': 0,
              'm': 0,
              'n': 0,
              'o': 0,
              'p': 0,
              'q': 0,
              'r': 0,
              's': 0,
              't': 0,
              'u': 0,
              'v': 0,
              'w': 0,
              'x': 0,
              'y': 0,
              'z': 0,
              }
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in alphabet:
            alphabet[lower_letter] += 1
    return alphabet



#opens the file and reads it
def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f'Error: the file at {path} was not found')
        return ""

main()