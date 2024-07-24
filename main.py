def main(): 
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    counter = count_words(text)
    print(counter)

def count_words(text):
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