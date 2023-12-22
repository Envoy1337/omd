LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('')
    ''
    
    # doctest: +ELLIPSIS
    >>> encode('123')
    '.---- ..--- ...--'
    >>> encode('_.&%$АБВ')
    Traceback (most recent call last):
        ...
    ValueError: Некорректные символы в сообщении
    """
    if not message:
        return ''

    if not message.isalpha() and not message.isdigit():
        raise ValueError('Некорректные символы в сообщении')

    encoded_signs = [LETTER_TO_MORSE.get(letter.upper(), '') for letter in message]
    return ' '.join(filter(bool, encoded_signs))
