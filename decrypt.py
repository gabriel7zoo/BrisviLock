import os
from cryptography.fernet import Fernet

# Decrypt a file
def decrypt_file(file_name, key):
    fernet = Fernet(key)

    # Define the path for the encrypted file
    encrypted_file_path = os.path.join('hidden_files', file_name)

    # Read the encrypted data
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted file back to the current directory
    decrypted_file_path = file_name[:-4]  # Remove .enc extension
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"File '{file_name}' has been decrypted and saved as '{decrypted_file_path}'.")

if __name__ == "__main__":
    file_to_decrypt = input("Enter the name of the encrypted file (with .enc): ")
    encryption_key = input("Enter the encryption key: ")
    decrypt_file(file_to_decrypt, encryption_key)
