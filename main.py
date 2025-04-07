import sys
from stats import sort_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        split = file_contents.split()
        letter_list = list(file_contents)

        characters = {}
        for letter in letter_list:
            if not letter.isalpha():
                continue

            lowercase_letter = letter.lower()
            if lowercase_letter in characters:
                characters[lowercase_letter] += 1
            else:
                characters[lowercase_letter] = 1

        sorted_chars = sort_character_counts(characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {len(split)} total words")
        print("--------- Character Count -------")
        
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['count']}")
        
        print("============= END ===============")
main()

