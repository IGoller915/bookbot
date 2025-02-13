def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    book_report = report(book_path, num_words, character_count)
    print(f"{book_report}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def report(book_path,num_words, character_count):
    character_report_text = character_report(character_count)
    report_text = f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n{character_report_text}\n--- End report ---"
    return report_text

def character_report(character_count):
    report_text = ""
    sorted_character_count = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    for i in sorted_character_count:
        if i[0].isalpha():
            report_text += f"The '{i[0]}' character was found {i[1]} times\n"
    return report_text
    



main()