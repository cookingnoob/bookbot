def main():
    try:
        book_path = 'books/frankenstein.txt'
        text = read_file(book_path)
        word_count = total_word_count(text)
        print(f"{word_count} words found in the document")
    except FileNotFoundError:
        print('file was not found')

def total_word_count(text):
    return len(text.split())

def read_file(book_path):
    with open(book_path) as f:
        return f.read()

main()


    # cwd = Path.cwd()
    # relative_path_books = '/books/frankenstein.txt'

    # f = open(f'{cwd}{relative_path_books}', "r")

    # print(f.read())