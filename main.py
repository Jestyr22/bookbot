def main():
    path = "./books/frankenstein.txt"
    book_contents = get_book_contents(path)
    word_count = get_word_count(book_contents)
    character_count = get_character_count(book_contents)
    print(f"There are {word_count} words in the document.")
    print(character_count)
    #Not asked for in the project, but adding some formatting can't hurt
    '''
    print("Here is a list of how many times each character appears:")
    #for character, count in character_count.items():
    #    print (f"{character}: {count}")
    '''
    #turns out adding formatting did hurt, will leave it as comments for future reference
    
   
def get_book_contents(path):
    with open(path) as f:
        contents = f.read()
    return(contents)

def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)

def get_character_count(book_contents):
    character_count_dict = {}
    lowercase_contents = book_contents.lower()
    for i in lowercase_contents:
        if i in character_count_dict:
            character_count_dict[i] += 1
        else:
            character_count_dict[i] = 1
    return character_count_dict
        

     

if __name__ == "__main__":
    main ()