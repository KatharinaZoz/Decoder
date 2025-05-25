DECRYPT_INPUT = 1
ENCRYPT_INPUT = 2
EXIT_INPUT = 3

running = True

def decrypt(value):
    pass

def encrypt(value):
    pass

while(running):
    try:
        choice = int(input("Choose: \n [1] Decrypt \n [2] Encrypt \n [3] Exit"))
    except ValueError:
        print("Choice invalid! Please try again...")
        continue
    
    if choice == EXIT_INPUT:
        print("Goodbye ^^")
        break

    try:    
        specs = int(input("[1] Enter value \n [2] Show all\n [3] Return"))
    except ValueError:
        print("Choice invalid! Returning...")
        continue

    if specs == EXIT_INPUT:
        print("Returning to Main Menu...")
        continue

    if choice == DECRYPT_INPUT:
    #TODO parse specs to int -> error handling      
        decrypt(specs)
    elif choice == ENCRYPT_INPUT:
    #TODO write input req for value or show all
        encrypt(specs)
    else:
        print("Invalid choice! Try again.")

