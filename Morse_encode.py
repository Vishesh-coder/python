MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   ' ': ' ',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

def encode(message):
    encoded_message = ''
    for letter in message.upper():
        if letter in MORSE_CODE:
            encoded_message += MORSE_CODE[letter] + ' '
        else:
            encoded_message += letter
    return encoded_message

if __name__ == '__main__':
    while True:
        message = input('Enter the message to encode (press Ctrl+C to exit): ')
        encoded_message = encode(message)
        print(f'Encoded message: {encoded_message}')