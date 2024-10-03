# BrisviLock

**BrisviLock** is a new-generation encryption lock for USB devices. Once your USB is connected to any device, it won't display the files uploaded using the **BrisviLock** script. The files are only viewable if you download **BrisviLock** and run the script to access them.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)

## Features

- **File Encryption**: Secure your files using strong encryption algorithms.
- **File Hiding**: Uploaded files won't be visible on the USB drive unless accessed through **BrisviLock**.
- **Cross-Platform**: Runs on any platform with Python installed.
- **User-Friendly CLI**: Simple command-line interface for ease of use.

## Installation

### Prerequisites

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository to your local machine or USB drive:

   ```bash
   git clone <your-repo-url>
   cd BrisviLock

3. Install the required Python packages:

pip install -r requirements.txt


4. Create a directory for hidden files:

mkdir hidden_files



Usage

1. Run the command-line interface:

python brisvi.py


2. Follow the prompts to encrypt or decrypt your files.



Commands

In brisvi.py

show: Displays a list of encrypted files in the hidden_files directory.

download_all: Decrypts all encrypted files in the hidden_files directory. Requires the encryption key.

exit: Exits the BrisviLock program.


In encrypt.py

File Encryption: Run the script and provide the path of the file you want to encrypt:

python encrypt.py


In decrypt.py

File Decryption: Run the script and provide the name of the encrypted file and the encryption key:

python decrypt.py


Disclaimer

Note: This software is in its early stages and has not been fully tested. Use it at your own risk. Please provide feedback and suggestions for improvements.

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to create a pull request or open an issue.


---

For any questions or support, please contact [your-email@example.com].

### How to Use

1. **Copy the above text** into a new file.
2. **Save the file as `README.md`** in the root of your **BrisviLock** project directory.

