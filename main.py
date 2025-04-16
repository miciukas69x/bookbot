import sys
from stats import number_of_words, characters_count, sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_text = f.read()
    return file_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = number_of_words(text)
    print (f"Found {num_words} total words.")
    char_counts = characters_count(text)
    sorted_characters = sorted_list(char_counts)
    print ("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()


