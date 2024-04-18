# Part I
 
def display_info(name):
    """Display various information about the user's name."""
    # 1. Display the number of characters in the string.
    print(f"Your name is {len(name)} characters long.")
 
    # 2. Display the last character in the string.
    print(f"The last character is: {name[-1]}")
 
    # 3. Display the location of the first occurrence of the letter 'e' (0 if not found).
    e_index = name.find('e')
    print(f"The first 'e' is at position {e_index if e_index != -1 else 0}.")
 
    # 4. Display the number of words in the string.
    num_words = len(name.split())
    print(f"The name has {num_words} {'word' if num_words == 1 else 'words'}.")
 
    # 5. Display the first word of the string.
    first_word = name.split()[0]
    print(f"The first word is {first_word}.")
 
    # 6. Display the number of vowels in the string.
    num_vowels = sum(1 for char in name if char.lower() in 'aeiou')
    print(f"The name contains {num_vowels} vowel{'s' if num_vowels != 1 else ''}.")
 
    # 7. Display the string after capitalizing all vowels in the string. All consonants should be lower case.
    modified_name = ''.join(char.upper() if char.lower() in 'aeiou' else char.lower() for char in name)
    print(f"The name with uppercase vowels is: {modified_name}")
 
    # 8. Display the string centered between 50 '~'s, and 70 '+'s.
    print('~' * 50 + name.center(len(name) + 100, '+') + '~' * 70)
 
    # 9. Display the string split in half on either end of 70 '*'s.
    half_length = len(name) // 2
    print(name[:half_length] + '*' * 70 + name[half_length:])
 
# Input name from the user
user_name = input("Please enter your name: ")
 
# Call the function to display information about the name
display_info(user_name)
 
# Gadsby by Ernest Vincent Wright (without the letter 'e')
gadsby_text = """
Quote goes here
"""
 
# Remove newlines and convert to lowercase
gadsby_text = gadsby_text.replace('\n', '').lower()
 
# Part II - Function A
 
def mirror_string(input_str):
    """Generate a string containing the original string and the string backwards."""
    return input_str + input_str[::-1]
 
# Test function A
print(mirror_string(gadsby_text))
 
# B- Write a function that removes all occurrences of a given letter from a string.
def remove_letter(input_str, letter):
    """Remove all occurrences of a given letter from a string."""
    return input_str.replace(letter, '')
 
# C- Write a function char_num that counts the number of alphabetic characters (a through
# z, or A through Z) in your text and then keeps track of how many are the letter ‘e’. Your
# function should print an analysis of the text like this: Your text contains 243 alphabetic
# characters, of which 109 (44.8%) are 'e'.
def char_num(input_str):
    """Count the number of alphabetic characters and occurrences of 'e' in the text."""
    alphabetic_count = sum(1 for char in input_str if char.isalpha())
    e_count = input_str.count('e')
    percentage_e = (e_count / alphabetic_count) * 100 if alphabetic_count != 0 else 0
    print(f"Your text contains {alphabetic_count} alphabetic characters, of which {e_count} ({percentage_e:.1f}%) are 'e'.")
 
# D- Modify the previous function to keep track of number of any character passed as a
# parameter are in the text. Try it with letter ‘e’. Did you get the same results?
def char_occurrences(input_str, char):
    """Count the occurrences of a given character in the text."""
    char_count = input_str.count(char)
    print(f"The text contains {char_count} occurrences of '{char}'.")
 
# E- Write a function called no_e that returns True if the given word doesn’t have the letter
# “e” in it.
def no_e(word):
    """Return True if the given word doesn't contain the letter 'e'."""
    return 'e' not in word
 
# F- Modify the previous function to return True if the passed word doesn’t have the
# character passed as another parameter. Call it for the same string and the letter ‘e’. Did
# you get the same results?
def no_character(word, char):
    """Return True if the given word doesn't contain the specified character."""
    return char not in word
 
# G- Modify your previous program to print only the words that have no “e” and compute
# the percentage of the words in the list have no “e.”
def words_without_e(text):
    """Print words from the text that don't contain the letter 'e'."""
    words = text.split()
    words_without_e = [word for word in words if 'e' not in word]
    percentage_no_e = (len(words_without_e) / len(words)) * 100 if len(words) != 0 else 0
    print(f"The percentage of words without 'e': {percentage_no_e:.2f}%")
    print("Words without 'e':", words_without_e)
 
# H- Write a function named avoids that takes a word and a string of forbidden letters, and
# that returns True if the word doesn’t use any of the forbidden letters.
def avoids(word, forbidden_letters):
    """Return True if the word doesn't use any of the forbidden letters."""
    return not any(letter in word for letter in forbidden_letters)
 
# I- Write a function named uses_only that takes a word and a string of letters, and that
# returns True if the word contains only letters in the list. Can you make a sentence using
# only the letters acefhlo? Other than “Hoe alfalfa?”
def uses_only(word, letters):
    """Return True if the word contains only letters from the given string."""
    return all(letter in letters for letter in word)
 
# J- Write a function named uses_all that takes a word and a string of required letters, and
# that returns True if the word uses all the required letters at least once. How many words
# are there that use all the vowels aeiou? How about aeiouy?
def uses_all(word, required_letters):
    """Return True if the word uses all the required letters at least once."""
    return all(letter in word for letter in required_letters)
 
# K- Write a function called is_abecedarian that returns True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abecedarian words are there?
def is_abecedarian(word):
    """Return True if the letters in a word appear in alphabetical order."""
    return all(word[i] <= word[i + 1] for i in range(len(word) - 1))
 
# Test the functions
# B
print(remove_letter("banana", "a"))  # Output: bnn
# C
char_num(gadsby_text)
# D
char_occurrences(gadsby_text, 'e')
# E
print(no_e("hello"))  # Output: False
# F
print(no_character("hello", "o"))  # Output: False
# G
words_without_e("Hello world, how are you?")  
# H
print(avoids("hello", "abc"))  # Output: False
# I
print(uses_only("hello", "acefhlo"))  # Output: True
# J
print(uses_all("hello", "aeiou"))  # Output: False
# K
print(is_abecedarian("abcde"))  # Output: True
 
# L- Write a function find that takes a character and finds the index where that character
# appears. If the character is not found, the function returns -1.
def find(character, word):
    """Find the index where the character appears in the word."""
    for i, char in enumerate(word):
        if char == character:
            return i
    return -1
 
# M- Modify find so that it has a third parameter, the index in word where it should start
# looking.
def find_with_start(character, word, start_index):
    """Find the index where the character appears in the word starting from the given index."""
    for i in range(start_index, len(word)):
        if word[i] == character:
            return i
    return -1
 
# N- Write a function called is_sorted that takes a string as a parameter and returns True if
# the string has the words sorted in ascending order and False otherwise.
def is_sorted(string):
    """Check if the words in the string are sorted in ascending order."""
    words = string.split()
    return all(words[i] <= words[i + 1] for i in range(len(words) - 1))
 
# O- Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are
# anagrams.
def is_anagram(word1, word2):
    """Check if two words are anagrams."""
    return sorted(word1) == sorted(word2)
 
# P- Write a function called has_duplicates that takes a string and returns True if there is any
# character that appears more than once in the string. It should not modify the original
# list.
def has_duplicates(string):
    """Check if there are any duplicates in the string."""
    return any(string.count(char) > 1 for char in set(string))
 
# Q- Write a function called remove_duplicates that takes a string and returns a new string
# with only the unique characters from the original.
def remove_duplicates(string):
    """Remove duplicate characters from the string."""
    return ''.join(set(string))
 
# Test the functions
# L
print(find('a', 'banana'))  # Output: 1
# M
print(find_with_start('a', 'banana', 2))  # Output: 3
# N
print(is_sorted("apple banana cherry"))  # Output: True
# O
print(is_anagram("listen", "silent"))  # Output: True
# P
print(has_duplicates("hello"))  # Output: True
# Q
print(remove_duplicates("hello"))  # Output: 'helo'
 