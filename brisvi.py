import os
import sys
from colorama import Fore, Style, init
from encrypt import encrypt_file
from decrypt import decrypt_file

# Initialize Colorama
init(autoreset=True)

def display_header():
    print(Fore.GREEN + Style.BRIGHT + "=======================")
    print(Fore.GREEN + Style.BRIGHT + "     BrisviLock       ")
    print(Fore.GREEN + Style.BRIGHT + "=======================")
    print(Fore.GREEN + "Secure File Encryption\n")

def show_files():
    print(Fore.YELLOW + "Encrypted files in the hidden_files directory:")
    for file in os.listdir('hidden_files'):
        if file.endswith('.enc'):
            print(Fore.CYAN + file)

def download_all():
    encryption_key = input(Fore.YELLOW + "Enter the encryption key for decryption: ")
    for file in os.listdir('hidden_files'):
        if file.endswith('.enc'):
            decrypt_file(file, encryption_key)
            print(Fore.GREEN + f"Decrypted '{file}'.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal for aesthetic
    display_header()
    
    while True:
        command = input(Fore.YELLOW + "\nEnter a command (show, download_all, exit): ")

        if command == 'show':
            show_files()
        elif command == 'download_all':
            download_all()
        elif command == 'exit':
            print(Fore.GREEN + "Exiting BrisviLock...")
            sys.exit()
        else:
            print(Fore.RED + "Invalid command. Try again.")

if __name__ == "__main__":
    main()
