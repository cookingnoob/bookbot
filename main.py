def main(): 
    path = 'books/frankenstei.txt'
    text = get_book_text(path)
    if text:
        counter = count_words(text)
    else:
        counter = 'Error: could not read the book'
    print(counter)

def count_words(text):
    if(len(text) == 0):
        return 'Could not count how many words the book has'
    words = text.split()
    return len(words)

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f'Error: the file at {path} was not found')
        return ""

main()