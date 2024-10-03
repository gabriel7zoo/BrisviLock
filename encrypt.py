import os
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a file
def encrypt_file(file_path):
    key = generate_key()
    fernet = Fernet(key)

    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)

    # Define the path for the encrypted file in the hidden_files directory
    encrypted_file_path = os.path.join('hidden_files', os.path.basename(file_path) + '.enc')

    # Save the encrypted file
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

    # Mark the original file as hidden (Windows)
    os.system(f'attrib +h "{file_path}"')  # This will hide the original file

    return key.decode(), encrypted_file_path  # Return the encryption key and path

if __name__ == "__main__":
    file_to_encrypt = input("Enter the path of the file to encrypt: ")
    encryption_key, encrypted_file = encrypt_file(file_to_encrypt)
    print(f"File '{file_to_encrypt}' has been encrypted and stored as '{encrypted_file}'. Encryption key: {encryption_key}")
