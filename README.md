# Password Generator

This is a simple password generator implemented in Python. It generates random passwords based on the specified length, combining letters (both uppercase and lowercase), digits, and punctuation marks. It also provides the option to save the generated password to a text file along with an optional note.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository or download the `pw_generator.py` file.

3. Open a terminal or command prompt and navigate to the directory where the `pw_generator.py` file is located.

4. Run the following command to execute the script:
'python pw_generator.py'


5. You will be prompted to enter the desired length of the password.

6. Once you enter the length, the program will generate a random password and display it on the console.

7. You will then be asked whether you want to save the generated password. Enter 'y' or 'Y' to proceed.

8. If you choose to save the password, you will be prompted to enter an optional note for that password.

9. The password and the note (if provided) will be saved in a file named `passwords.txt` in the same directory as the script. The file will be created if it doesn't exist.

10. You can run the script multiple times to generate different passwords with varying lengths and save them to the `passwords.txt` file.

## Customization

You can customize the password generation process and file-saving behavior by modifying the code:

- Adjust the characters used for password generation:
- The `characters` string in the `generate_password` function includes ASCII letters, digits, and punctuation marks. You can add or remove characters to fit your requirements.

- Change the save file name:
- The file name and path for saving the passwords is set to `passwords.txt`. If you want to use a different name or location, you can modify the `save_password` function.

## Example

Here's an example of running the password generator script:
    
    
    $ python pw_generator.py

    Enter the length of the password: 12
    
    Generated Password: f8X{32D$>3q
    
    Do you want to save this password? (y/n): y
    
    Enter a note for this password: Social Media
    
    Password saved successfully.
