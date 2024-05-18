from itertools import permutations
import random
import sys
import time
import string
import re
import os
import traceback


def print_robco_logo():
    robco_logo = [
        "                         ---------------------------------------------------                         ",
        "                         ---------------------------------------------------                         ",
        "                                          *** CLASSIFIED ***                                         ",
        "                         ---------------------------------------------------                         ",
        "                         ---------------------------------------------------                         ",
        "                         ________              ___          ____                                     ",
        "                         `MMMMMMMb.             MM         6MMMMb/                                   ",
        "                          MM    `Mb             MM        8P    YM                                   ",
        "                          MM     MM    _____    MM____   6M      Y   _____                           ",
        "                          MM     MM   6MMMMMb   MMMMMMb  MM         6MMMMMb                          ",
        "                          MM    .M9  6M'   `Mb  MM'  `Mb MM        6M'   `Mb                         ",
        "                          MMMMMMM9'  MM     MM  MM    MM MM        MM     MM                         ",
        "                          MM  \M\    MM     MM  MM    MM MM        MM     MM                         ",
        "                          MM   \M\   MM     MM  MM    MM YM      6 MM     MM                         ",
        "                          MM    \M\  YM.   ,M9  MM.  ,M9  8b    d9 YM.   ,M9                         ",
        "                         _MM_    \M\_ YMMMMM9  _MYMMMM9    YMMMM9   YMMMMM9                          ",
        "                         ---------------------------------------------------                         ",
        "                         ---------------------------------------------------                         ",
        "                                          *** CLASSIFIED ***                                         ",
        "                         ---------------------------------------------------                         ",
        "                         ---------------------------------------------------                         ",
        "                              ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM                              ",
        "                               COPYRIGHT 2075-2077 ROBCO INDUSTRIES       \n                         ",
    ]

    # Print each line of the logo with variable delays
    for line in robco_logo:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(random.uniform(0.001, 0.002))  # Random delay between 10ms and 30ms
        print()


def load_dictionary():
    try:
        # Get the path to the dictionary file
        if getattr(sys, 'frozen', False):
            # If the application is frozen (e.g., PyInstaller executable)
            dictionary_file_path = os.path.join(sys._MEIPASS, 'dictionary.txt')
        else:
            # If the application is not frozen (e.g., running as a script)
            dictionary_file_path = 'dictionary.txt'

        with open(dictionary_file_path, 'r') as file:
            content = file.read()
            words = set(word.strip().lower() for word in content.split(','))
        return words
    except FileNotFoundError:
        # Log the error
        with open("error.log", "a") as f:
            f.write("Dictionary file not found at the specified path: {}\n".format(dictionary_file_path))
        # Raise the error again to propagate it
        raise


def find_anagrams(word, dictionary):
    word = word.lower()
    perms = {''.join(p) for p in permutations(word)}
    return perms.intersection(dictionary)


def print_loading_bar(leading_spaces):
    bar_length = 50
    duration = random.randint(2, 6)
    increment = duration / bar_length
    leading_spaces //= 2  # Reduce leading spaces by half

    for i in range(bar_length + 1):
        percent_complete = (i / bar_length) * 100
        bar = '#' * i + '-' * (bar_length - i)
        sys.stdout.write(f'\r{" " * leading_spaces}[{bar}] {percent_complete:.2f}%')
        sys.stdout.flush()
        time.sleep(increment)
    print()


def print_cipher_table(alphabet, encoded_alphabet, inputs, user_input_phrase):
    table_width = 4 * len(alphabet) + 1
    header = "CIPHER TABLE"
    header_spaces = (table_width - len(header)) // 2
    print(" " * header_spaces + "CODE PHRASE: " + user_input_phrase)
    print(" " * header_spaces + header)
    print("_" * table_width)
    alphabet_row = "| " + " | ".join(alphabet) + " |"
    print(alphabet_row)
    encoded_alphabet_row = "| " + " | ".join(encoded_alphabet) + " |"
    print(encoded_alphabet_row)
    print("¯" * table_width)
    title = "ENCRYPTED KEY PAIRS"
    title_spaces = (table_width - len(title)) // 2
    print(" " * title_spaces + title)
    key_values_width = 4 * len(inputs) + 1
    leading_spaces = (table_width - key_values_width) // 2
    print(" " * leading_spaces + "_________________________________")
    print(" " * leading_spaces + "| " + " | ".join(list(inputs.keys())) + " |")
    print(" " * leading_spaces + "| " + " | ".join(list(inputs.values())) + " |")
    print(" " * leading_spaces + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("\n")
    return leading_spaces


def print_decrypted_pairs(decrypted_pairs, leading_spaces):
    key_values_width = 4 * len(decrypted_pairs) + 1
    title = "DECRYPTED KEY PAIRS"
    title_spaces = (key_values_width - len(title)) // 2
    total_spaces = leading_spaces + title_spaces
    print("\n")
    print(" " * total_spaces + title)
    print(" " * leading_spaces + "_________________________________")
    print(" " * leading_spaces + "| " + " | ".join(list(decrypted_pairs.keys())) + " |")
    print(" " * leading_spaces + "| " + " | ".join(list(decrypted_pairs.values())) + " |")
    print(" " * leading_spaces + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("\n")


def print_possible_launch_code(anagram, decrypted_pairs, leading_spaces, confidence_value):
    key_values_width = 4 * len(anagram) + 1
    title = "-- ** POSSIBLE LAUNCH CODE ** --"
    title_spaces = (key_values_width - len(title)) // 2
    total_spaces = leading_spaces + title_spaces
    print("\n")
    print(" " * total_spaces + title)
    print(" " * leading_spaces + "_________________________________")
    print(" " * leading_spaces + "| " + " | ".join(list(anagram)) + " |")
    print(" " * leading_spaces + "| " + " | ".join([decrypted_pairs[letter] for letter in anagram]) + " |")
    print(" " * leading_spaces + "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("\n")
    confidence_message = f"CONFIDENCE IN AUTHENTICITY: {confidence_value:.4f}%"
    print(" " * (total_spaces + key_values_width // 2 - len(confidence_message) // 2) + confidence_message)
    print("\n")

def decrypt_pairs(encoded_alphabet, inputs):
    # Create a dictionary to store the decrypted pairs
    decrypted_pairs = {}

    # Iterate through each letter in the encrypted pairs
    for letter, number in inputs.items():
        # Find the index of the letter in the encoded alphabet
        index = encoded_alphabet.index(letter)
        # Use the index to find the corresponding letter in the original alphabet
        original_letter = string.ascii_uppercase[index]
        # Store the decrypted pair in the dictionary
        decrypted_pairs[original_letter] = number

    return decrypted_pairs


def validate_input(input_str, existing_inputs):
    # Regular expression pattern to match the allowed format
    pattern = r'^[A-Za-z]-\d$|^[A-Za-z]\d$'

    # Check if the input matches the pattern
    if not re.match(pattern, input_str):
        return False

    # Convert the input letter to uppercase
    input_letter = input_str[0].upper()

    # Check for duplicate letters across existing inputs
    for existing_input in existing_inputs:
        existing_letter = existing_input[0].upper()
        if existing_letter == input_letter:
            print("WARNING: ENSURE INPUT KEYS ARE TAGGED FOR THE SAME SILO AND ARE NOT USING THE SAME LETTERS!")
            return True  # Return True to allow continuation
    return True


def validate_input(input_str, existing_inputs):
    # Regular expression pattern to match the allowed format
    pattern = r'^[A-Za-z]-\d$|^[A-Za-z]\d$'

    # Check if the input matches the pattern
    if not re.match(pattern, input_str):
        return False

    # Convert the input letter to uppercase
    input_letter = input_str[0].upper()

    # Check for duplicate letters across existing inputs
    for existing_input in existing_inputs:
        existing_letter = existing_input[0].upper()
        if existing_letter == input_letter:
            print("WARNING: ENSURE INPUT KEYS ARE TAGGED FOR THE SAME SILO AND ARE NOT USING THE SAME LETTERS!")
            return True  # Return True to allow continuation
    return True


def format_input(input_str):
    # Regular expression pattern to match the allowed formats
    pattern = r'^[A-Za-z]-\d$|^[A-Za-z]\d$'

    # If the input matches the format, return it unchanged
    if re.match(pattern, input_str):
        return input_str.upper()

    # If the input doesn't match the format, try to fix it
    else:
        # Remove any non-alphanumeric characters
        input_str = re.sub(r'[^A-Za-z\d]', '', input_str)
        # Split the input into letter and number
        letter = input_str[0].upper()
        number = input_str[1:]
        return {letter: number}


def get_valid_input(prompt, existing_inputs):
    while True:
        user_input = input(prompt)
        if validate_input(user_input, existing_inputs):
            return format_input(user_input)
        else:
            print("ERROR: INPUT NOT RECOGNIZED, RENTER VALUE!!!")


def get_user_inputs():
    print("Please enter 8 values in the format 'Letter-Number' or 'LetterNumber', e.g., 'T-6' or 'T6':")
    inputs = {}
    for i in range(1, 9):
        prompt = f"Enter Key {i}: "
        valid_input = get_valid_input(prompt, inputs)
        inputs[valid_input[0]] = valid_input[2:]
    return inputs

def combine_letters(decrypted_pairs):
    # Combine the letters from decrypted key pairs
    combined_letters = ''.join(decrypted_pairs.keys())

    return combined_letters


# Assuming you have a function to solve anagrams
def solve_anagram(word, dictionary):
    perms = {''.join(p) for p in permutations(word)}
    return perms.intersection(dictionary)


def main():
    try:
        print_robco_logo()
        while True:
            alphabet = list(string.ascii_uppercase)
            user_input_phrase = input("Enter the code-phrase: ")
            code_phrase = list(user_input_phrase.upper())
            delta_alphabet = [letter for letter in alphabet if letter not in code_phrase]
            encoded_alphabet = code_phrase + delta_alphabet

            inputs = get_user_inputs()
            leading_spaces = print_cipher_table(alphabet, encoded_alphabet, inputs, user_input_phrase)
            print_loading_bar(leading_spaces)

            decrypted_pairs = decrypt_pairs(encoded_alphabet, inputs)
            print_decrypted_pairs(decrypted_pairs, leading_spaces)

            decrypted_word = ''.join(decrypted_pairs.keys())
            dictionary = load_dictionary()
            anagrams = find_anagrams(decrypted_word, dictionary)

            if anagrams:
                print(f'{" " * leading_spaces}Decrypted Word: {decrypted_word.upper()}' + "\n")
                print_loading_bar(leading_spaces)
                anagram = next(iter(anagrams))  # Choose the first anagram found
                print(f'{" " * leading_spaces}PERMUTATION FOUND: {anagram.upper()}' + "\n")
                confidence_value = random.uniform(65, 95)  # Generate a floating-point value with 4 degrees of precision
                print_possible_launch_code(anagram.upper(), decrypted_pairs, leading_spaces, confidence_value)
            else:
                print(f"WARNING: No permutations of '{decrypted_word}' found. Re-check inputs.")

            # Prompt the user to enter another phrase and set of keys
            retry = input("Would you like to enter another phrase and set of keys? (y/n): ").strip().lower()
            if retry not in ['y', 'yes']:
                print("Exiting application. Thank you!")
                break

    except Exception as e:
        # Log the traceback to a file
        with open("error.log", "a") as f:
            traceback.print_exc(file=f)
        print("An unexpected error occurred. Please check the error.log file for details.")

    # Prompt the user to press Enter to exit
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()


# Enter Key 1: T-6
# Enter Key 2: Y-1
# Enter Key 3: X-6
# Enter Key 4: K-2
# Enter Key 5: H-9
# Enter Key 6: E-5
# Enter Key 7: L-4
# Enter Key 8: Q-5