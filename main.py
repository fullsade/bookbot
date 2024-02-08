def main():
    book_path = "books/frankenstein.txt"
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = get_text(book_path)
    words_in_book = count_words(text)
    letters_in_books = count_letters(text)
    sorted_chars = sort_chars(letters_in_books)
    print(text)
    print()
    print("---")
    print()
    print(f"There are {words_in_book} words in this book.")
    print()
    print(letters_in_books)
    print()
    for ch in sorted_chars:
            print(f"The '{ch['char']}' character was found {ch['num']} times")
    print()
    print("---")
    print()

def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def sort_on(d):
    return d["num"]

def count_letters(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters_dict = {letter: 0 for letter in alphabet}
    for letter in text.lower():
        if letter in alphabet:
            letters_dict[letter] += 1
    return letters_dict

def sort_chars(dict):
    sorted = []
    for ch in dict:
        sorted.append({"char": ch, "num": dict[ch]})
    sorted.sort(reverse=True, key=sort_on)
    
    return sorted
    
main()