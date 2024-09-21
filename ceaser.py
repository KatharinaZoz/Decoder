DECRYPT_INPUT = "1"
ENCRYPT_INPUT = "2"
EXIT_INPUT = "X"

running = True

def decrypt(value):
    pass

def encrypt(value):
    pass

while(running):
    choice = input("Choose: \n [1] Decrypt \n [2] Encrypt \n [X] Exit")

    specs = input("[1] Enter value \n [2] Show all")
    if choice == DECRYPT_INPUT:
    #TODO write input req for value or show all
        pass
    elif choice == ENCRYPT_INPUT:
    #TODO write input req for value or show all
        pass
    elif choice.upper() == EXIT_INPUT:
        running = false
    else:
        print("Invalid choice! Try again.")

