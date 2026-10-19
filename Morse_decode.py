MORSE_CODE = {
    '.-': 'A',   '-...': 'B',   '-.-.': 'C',
    '-..': 'D',  '.': 'E',      '..-.': 'F',
    '--.': 'G',  '....': 'H',   '..': 'I',
    '.---': 'J', '-.-': 'K',    '.-..': 'L',
    '--': 'M',   '-.': 'N',     '---': 'O',
    '.--.': 'P', '--.-': 'Q',   '.-.': 'R',
    '...': 'S',  '-': 'T',      '..-': 'U',
    '...-': 'V', '.--': 'W',    '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',   ' ': ' ',
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

def decode(message):
    message += ' '
    decoded_message = ''
    decipher = ''
    for letter in message:
        if letter != ' ':
            i = 0
            decipher += letter
        else:
            i += 1
            if i == 2:
                decoded_message += ' '
            else:
                decoded_message += MORSE_CODE.get(decipher, decipher)
                decipher = ''
    return decoded_message

if __name__ == '__main__':
    while True:
        message = input('Enter the message to decode (press Ctrl+C to exit): ')
        decoded_message = decode(message)
        print(f'Decoded message: {decoded_message}')
