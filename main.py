def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_in_book = count_words(text)
    letters_in_books = count_letters(text)
    print(text)
    print(f"{words_in_book} words in this book!")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letters(text):
    return None
    
main()