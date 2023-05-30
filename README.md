# Password Generator

This is a simple password generator implemented in Python. It generates random passwords based on the specified length, combining letters (both uppercase and lowercase), digits, and punctuation marks.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository or download the `password_generator.py` file.

3. Open a terminal or command prompt and navigate to the directory where the `password_generator.py` file is located.

4. Run the following command to execute the script: "python password_generator.py"


5. You will be prompted to enter the desired length of the password.

6. Once you enter the length, the program will generate a random password and display it on the console.

7. You can run the script multiple times to generate different passwords with varying lengths.

## Customization

You can customize the password generation process by modifying the code:

- Adjust the characters used for password generation:
- The `characters` string in the `generate_password` function includes ASCII letters, digits, and punctuation marks. You can add or remove characters to fit your requirements.

- Modify the default password length:
- The `password_length` variable in the `main` function specifies the default length of the generated password. You can change this value to a different integer.

## Example

Here's an example of running the password generator script:

$ python password_generator.py
Enter the length of the password: 12
Generated Password: f8X{32D$>3q


In this case, the user entered a length of 12, and the program generated a password "f8X{32D$>3q".

## License

This project is licensed under the [MIT License](LICENSE).
