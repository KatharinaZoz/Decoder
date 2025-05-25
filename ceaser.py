DECRYPT_INPUT = 1
ENCRYPT_INPUT = 2
EXIT_INPUT = 3

INVALID_CHOICE_ERROR="Choice invalid! Please try again... \n"

running = True

def decrypt(value):
    pass

def encrypt(value):
    pass

def handleEncrypt():
    pass

def handleDecrypt():
    pass



while(running):
    try:
        choice = int(input("Choose: \n [1] Decrypt \n [2] Encrypt \n [3] Exit \n"))
    except ValueError:
        print(INVALID_CHOICE_ERROR)
        continue
    
    if choice == EXIT_INPUT:
        print("Goodbye ^^")
        break
    elif choice <1 or choice > 3:
        print(INVALID_CHOICE_ERROR)
        continue

    filler = "cypher" if choice == 1 else "message"
    text = input("Please enter the {}: \n".format(filler))

    try:    
        specs = int(input(" [1] Enter value \n [2] Show all\n [3] Return \n"))
    except ValueError:
        print(INVALID_CHOICE_ERROR)
        continue

    if specs == EXIT_INPUT:
        print("Returning to Main Menu...")
        continue
    elif specs <1 or specs > 3:
        print(INVALID_CHOICE_ERROR)
        continue
    elif specs == 1:
        try:
            value = int(input("Enter value: \n"))
        except ValueError:
            print(INVALID_CHOICE_ERROR)
            continue


    if choice == DECRYPT_INPUT:
        decrypt(specs)
    elif choice == ENCRYPT_INPUT:
        encrypt(specs)

