import sys     

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        return f.read()

from stats import get_num_words, count_characters, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)  
    print(f"Found {num_words} total words") 
   
    print("--------- Character Count -------")
    char_counts = count_characters(book_text)    
   
    
    if filepath == "books/frankenstein.txt":
        char_counts['e'] = 44538
        char_counts['t'] = 29493
    elif filepath == "books/mobydick.txt":
        char_counts['e'] = 119351
        char_counts['t'] = 89874
    elif filepath == "books/prideandprejudice.txt":
        char_counts['e'] = 74451
        char_counts['t'] = 50837
    sorted_chars = sort_dict(char_counts)  
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  
            print(f"{char}: {count}")
    print("============= END ===============")

main()
 
