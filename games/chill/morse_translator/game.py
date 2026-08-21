AUTHOR = "Dartkins"

char_to_morse = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    # Standard ITU-R Punctuation
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '/': '-..-.', ':': '---...', "'": '.----.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-',
    '"': '.-..-.', '=': '-...-', '+': '.-.-.',
    '@': '.--.-.',
    # Non-Standard Punctuation
    '!': '-.-.--', '&': '.-...', ';': '-.-.-.',
    '_': '..--.-', '$': '...-..-',
    # Functional
    ' ': '/', '': ''
}
morse_to_char = {morse: char for char, morse in char_to_morse.items()}

def choose_mode():
    """Display options menu and returns the user's choice"""
    print('''
Choose an option:

[1] Encode text
[2] Decode Morse
[3] Quit\n''')
    # Keep asking until a valid menu option is entered
    while (mode := input('> ')) not in ('1', '2', '3'):
        print("Invalid option. Please enter 1, 2, or 3.")
    return mode

def validate_string(message, mode):
    """Return True if every character in the message is valid for the translation direction"""
    if mode == '1':
        comparison_list = char_to_morse.keys()
    else:
        comparison_list = morse_to_char.keys()
    invalid_chars = set(char for char in message if char not in comparison_list)
    if invalid_chars:
        print(f'Invalid character(s): {", ".join(invalid_chars)}')
        return False
    return True

def run():
    print(f'Morse Code Translator by {AUTHOR}')
    
    mode = choose_mode()
    
    while mode != '3':
        translated_message = ''

        # Encode logic
        if mode == '1':
            while not (validate_string(message := input('Enter string to translate: ').upper(), mode)):
                pass
            for char in message.upper():
                translated_message += char_to_morse.get(char, '?') + ' '

        # Decode logic
        else:
            while not (validate_string(message := input('Enter Morse code to translate: ').split(' '), mode)):
                pass
            for morse in message:
                translated_message += morse_to_char[morse]
                
        print(translated_message)
        mode = choose_mode()

