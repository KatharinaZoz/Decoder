DECRYPT_INPUT = 1
ENCRYPT_INPUT = 2
EXIT_INPUT = 3
OFFSET_INPUT = 1
SHOW_ALL_INPUT = 2
RETURN_INPUT = 3

INVALID_CHOICE_ERROR="Choice invalid! Please try again... \n"
OUTPUT_MESSAGE="Offset {}: \n    {}"

ALPHABET="abcdefghijklmnopqrstuvwxyz"

running = True

#decrypts a cypher with a single offset value
def decrypt(text: str, offset:int) -> str:
    message = ""
    for letter in text:
        index = ALPHABET.find(letter.lower())
        index = (index - offset + 26) % 26
        decodedLetter = ALPHABET[index]
        message += decodedLetter.upper() if letter.isupper() else decodedLetter
    return message

#encrypts a text using a single offset value
def encrypt(text: str, offset:int) -> str:
    message = ""
    for letter in text:
        index = ALPHABET.find(letter.lower())
        index = (index + offset) % 26
        encodedLetter = ALPHABET[index]
        message += encodedLetter.upper() if letter.isupper() else encodedLetter
    return message

#handles the decrypt management with single decrypt and show all decrypt
def handleDecrypt(text: str, offset: int) -> None:
    if offset != -1: #if user chose offset
        print(OUTPUT_MESSAGE.format(offset, decrypt(text, offset - 1)))
    else:
        for index in range(1,27): #if user chose "show all"
            print(OUTPUT_MESSAGE.format(index, decrypt(text, index - 1)))

#handles the encrypt management with single encrypt and show all encrypt
def handleEncrypt(text: str, offset: int) -> None:
    if offset != -1: #if user chose offset
        print(OUTPUT_MESSAGE.format(offset, encrypt(text, offset - 1)))
    else:
        for index in range(1,27): #if user chose "show all"
            print(OUTPUT_MESSAGE.format(index, encrypt(text, index - 1)))

#helper method to get user input that needs to be convertable to int
def get_int_input(prompt: str) -> int | None:
    try:
        choice = int(input(prompt))
    except ValueError:
        print(INVALID_CHOICE_ERROR)
        return None
    return choice

#if user chooses to input a offset value
def get_offset() -> int:
    offset = get_int_input("Enter offset: \n")
    if offset is None:
        return -1
    return abs(offset) % 26
    
def handleMainMenu() -> None:
    while(running):

        #choose main function: decrypt cyphertext or encrypt message
        choice = get_int_input("Choose: \n [1] Decrypt \n [2] Encrypt \n [3] Exit \n")
        if choice is None:
            continue
        elif choice == EXIT_INPUT:
            print("Goodbye ^^")
            break
        elif choice < DECRYPT_INPUT or choice > EXIT_INPUT:
            print(INVALID_CHOICE_ERROR)
            continue

        text_label = "cypher" if choice == DECRYPT_INPUT else "message"
        text = input("Please enter the {}: \n".format(text_label))

        offset = -1
        
        #choose weather to de-/encrypt with a specific key or show all possible de-/encryptions
        offset_choice = get_int_input(" [1] Enter offset \n [2] Show all\n [3] Return \n")
        if offset_choice is None:
            continue
        elif offset_choice == EXIT_INPUT:
            print("Returning to Main Menu...")
            continue
        elif offset_choice < OFFSET_INPUT or offset_choice > RETURN_INPUT:
            print(INVALID_CHOICE_ERROR)
            continue
        elif offset_choice == OFFSET_INPUT:
            offset = get_offset()
            

        if choice == DECRYPT_INPUT:
            handleDecrypt(text, offset)
        elif choice == ENCRYPT_INPUT:
            handleEncrypt(text, offset)

handleMainMenu()
