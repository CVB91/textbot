def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_letters(text)
    occurance = sort_characters_by_occurrence(count)
    print(occurance)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count +=1
    
    return count

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def sort_characters_by_occurrence(letter_count):
    count_list = [{"char": char, "num": count} for char, count in letter_count.items()]
    count_list.sort(reverse=True, key=lambda x: x['num'])
    return count_list



main()