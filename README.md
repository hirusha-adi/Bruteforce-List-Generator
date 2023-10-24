# Bruteforce List Generator

## Description
BruteList is a Python script designed for generating a list of potential passwords based on the specified character set and password length. It can be used for various purposes, including password cracking, penetration testing, or generating wordlists for security assessments. BruteList allows you to customize the character set to include numbers, lowercase letters, uppercase letters, and special characters, as well as control the output method.

## Features
- Customizable character set: You can specify which character types to include in the password generation process, including numbers (0-9), lowercase letters (a-z), uppercase letters (A-Z), and special characters.
- Password length: You can set the desired length for the generated passwords.
- Output options: BruteList provides two output options - you can either print the generated passwords to the console or save them to a file.
- Verbose mode: In verbose mode, the script will print each generated combination to the console.
- Output to a file: You can specify the name of the output file, and BruteList will save the generated passwords to that file.

## Prerequisites
- Python 3.x

## Usage
To use BruteList, follow these steps:

1. Clone or download the BruteList repository to your local machine.

2. Open a terminal and navigate to the directory where the BruteList script is located.

3. Run the BruteList script with the desired options:

   ```
   usage: brutelist [-h] [-i] [-a] [-A] [-p] [-v] [-f FILE] [-l LENGTH]

   options:
   -h, --help            show this help message and exit
   -i, --int             Use numbers (0-9)
   -a, --alphabet        Use letters (a-z)
   -A, --ALPHABET        Use letters (A-Z)
   -p, --punctuation     32 special characters
   -v, --verbose         Print every combination on the screen
   -f FILE, --file FILE  Output to a file
   -l LEN, --length LEN  Length of the password
   ```

4. Customize the character set to include the desired character types by using the `-i`, `-a`, `-A`, and `-p` options.

5. Set the password length using the `-l` option.

6. Choose the output method: either print the passwords to the console with `-v` or save them to a file with `-f`.

7. If you choose to save the passwords to a file, provide a filename using the `-f` option.

8. Run the script, and it will generate the list of passwords based on your specifications.

## Examples
Here are some example usages of BruteList:

1. Generate all possible 4-digit PIN codes and save them to a file named "pin_codes.txt":
   ```
   python3 brutelist.py -i -l 4 -f pin_codes.txt
   ```

2. Generate passwords containing lowercase letters and numbers, each with a length of 6 characters, and display them on the console:
   ```
   python3 brutelist.py -a -i -l 6 -v
   ```

3. Generate complex passwords including lowercase and uppercase letters, numbers, and special characters, each with a length of 8 characters, and save them to a file named "complex_passwords.txt":
   ```
   python3 brutelist.py -a -A -i -p -l 8 -f complex_passwords.txt
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to [OpenAI](https://www.openai.com/) for the GPT-3.5 model used to generate this README.
