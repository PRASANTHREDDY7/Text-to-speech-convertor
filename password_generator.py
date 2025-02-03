import random
import string     
length = int(input("Enter the password length: "))
check = input("Do you want to customize the cases and numbers (or) let me generate randomly for you? (y/n): ").lower()
if check == "y":  # Fixed condition
    ask_upper = input("Do you want to include uppercase letters? (y/n): ").lower()
    ask_lower = input("Do you want to include lowercase letters? (y/n): ").lower()
    ask_numbers = input("Do you want to include numbers? (y/n): ").lower()
    ask_symbols = input("Do you want to include special characters? (y/n): ").lower()
    characters = " "
    if ask_upper == "y":  # Fixed condition
        characters += string.ascii_uppercase
    if ask_lower == "y":
        characters += string.ascii_lowercase    
    if ask_numbers == "y":
        characters += string.digits
    if ask_symbols == "y":
        characters += string.punctuation
    if characters:  # Ensuring at least one character set is chosen
        password = ''.join(random.choices(characters, k=length))
        print("Generated Password is:", password)
    else:
        print("You did not select any character type. Cannot generate a password.")
elif check == "n":
    password1 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    print("Generated Password is:", password1)
else:
    print("Enter 'y' or 'n' only.")
