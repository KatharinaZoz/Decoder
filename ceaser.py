DECRYPT_INPUT = 1
ENCRYPT_INPUT = 2
EXIT_INPUT = 3

INVALID_CHOICE_ERROR="Choice invalid! Please try again... \n"
OUTPUT_MESSAGE="Offset {}: \n    {}"

ALPHABET="abcdefghijklmnopqrstuvwxyz"

running = True

def decrypt(text: str, offset:int) -> str:
    message = ""
    for letter in text:
        index = ALPHABET.find(letter.lower())
        index = (index - offset + 26) % 26
        decodedLetter = ALPHABET[index]
        message += decodedLetter.upper() if letter.isupper() else decodedLetter
    return message


def encrypt(text: str, offset:int) -> str:
    message = ""
    for letter in text:
        index = ALPHABET.find(letter.lower())
        index = (index + offset) % 26
        encodedLetter = ALPHABET[index]
        message += encodedLetter.upper() if letter.isupper() else encodedLetter
    return message

def handleDecrypt(text: str, offset: int):
    if offset != -1:
        print(OUTPUT_MESSAGE.format(offset, decrypt(text, offset - 1)))
    else:
        for index in range(1,27):
            print(OUTPUT_MESSAGE.format(index, decrypt(text, index - 1)))


def handleEncrypt(text: str, offset: int):
    if offset != -1:
        print(OUTPUT_MESSAGE.format(offset, encrypt(text, offset - 1)))
    else:
        for index in range(1,27):
            print(OUTPUT_MESSAGE.format(index, encrypt(text, index - 1)))



while(running):
    try:
        choice = int(input("Choose: \n [1] Decrypt \n [2] Encrypt \n [3] Exit \n"))
    except ValueError:
        print(INVALID_CHOICE_ERROR)
        continue
    
    if choice == EXIT_INPUT:
        print("Goodbye ^^")
        break
    elif choice < 1 or choice > 3:
        print(INVALID_CHOICE_ERROR)
        continue

    filler = "cypher" if choice == 1 else "message"
    text = input("Please enter the {}: \n".format(filler))

    try:    
        specs = int(input(" [1] Enter offset \n [2] Show all\n [3] Return \n"))
    except ValueError:
        print(INVALID_CHOICE_ERROR)
        continue

    offset = -1

    if specs == EXIT_INPUT:
        print("Returning to Main Menu...")
        continue
    elif specs < 1 or specs > 3:
        print(INVALID_CHOICE_ERROR)
        continue
    elif specs == 1:
        try:
            offset = int(input("Enter offset: \n"))
        except ValueError:
            print(INVALID_CHOICE_ERROR)
            continue
        if offset < 0:
            print("Calculating positive offset equivalent...")
            offset *= -1
        if offset > 26:
            offset %= 26
    if choice == DECRYPT_INPUT:
        handleDecrypt(text, offset)
    elif choice == ENCRYPT_INPUT:
        handleEncrypt(text, offset)

